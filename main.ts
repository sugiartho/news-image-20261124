// news-image-20261124 entry (Node 22, standard library only).
//
// The front page is drawn by draw.py and stored as entry.png next to
// this file. This program's only job is to place that exact image at
// /output/entry.png for the grader. It reads the file, checks it is a
// whole PNG under the 1 MiB cap, and writes the same bytes out again,
// so the run is deterministic: identical input bytes, identical output.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { existsSync, mkdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1024 * 1024; // the competition's 1 MiB cap
const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

if (!existsSync(source)) {
  throw new Error("entry.png is missing next to main.ts; run draw.py first");
}
const png = readFileSync(source);
const pngMagic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (png.length < 8 || !png.subarray(0, 8).equals(pngMagic)) {
  throw new Error("entry.png does not start with the PNG signature");
}
if (png.length > MAX_BYTES) {
  throw new Error(`entry.png is ${png.length} bytes, over the 1 MiB cap`);
}
// The competition also caps the image at 1024x1024 pixels: read the
// width/height straight out of the PNG IHDR chunk (bytes 16-23) so a
// too-large image fails here with a clear message instead of at the gate.
const width = png.readUInt32BE(16);
const height = png.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 cap`);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(target, png);
const written = statSync(target).size;
// Read the output back and compare byte for byte: the grader runs this
// program twice and both runs must produce identical bytes, so prove the
// copy is exact here instead of trusting the write call alone.
const roundTrip = readFileSync(target);
if (!roundTrip.equals(png)) {
  throw new Error("round-trip check failed: output bytes differ from entry.png");
}
console.log(`news-image-20261124: copied ${png.length} bytes to ${target} (verified ${written} bytes on disk, ${width}x${height})`);
