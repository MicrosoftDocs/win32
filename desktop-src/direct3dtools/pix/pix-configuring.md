---
title: Configuring PIX
ms.topic: article
description: Documentation on various ways to configure PIX.
---

# Configuring PIX
PIX has various options you can use to customize PIX to your liking. Most of these are accessed in the Settings menu (accessed via the main File menu).

## Debug symbols
When debugging shaders or profiling CPU code you'll want to provide PIX with debug symbols (PDBs) to enable function names and source code mappings. You can configure where PIX looks for these files in Settings under "Symbol / PDB Options".

For details on how to generate appropriate PDBs, check out https://devblogs.microsoft.com/pix/configuring-pix-to-access-pdbs-for-cpu-captures/.
