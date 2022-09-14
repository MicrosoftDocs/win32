---
description: Pktextract.exe is a tool that extracts the publicKeyToken attribute from a certificate file.
ms.assetid: 195ff5bd-bb60-4053-9308-ceacd29853c0
title: Pktextract.exe
ms.topic: article
ms.date: 05/31/2018
---

# Pktextract.exe

Pktextract.exe is a tool that extracts the **publicKeyToken** attribute from a certificate file. The output is the **publicKeyToken**, which is a unique 16-character (8-byte) identifier of the public key present in the certificate, in a format that can easily be pasted into an assembly identity statement. The certificate file must be present in the same directory as Pktextract.exe to use the utility. Pktextract.exe is provided in the Microsoft Windows Software Development Kit (SDK).

## Syntax

**pktextract.exe** *<filename.cer>* **\[-quiet\] \[-nologo\]**

## Command Line Options

Pktextract.exe uses the following case-insensitive command line options.



| Option  | Description                                                          |
|---------|----------------------------------------------------------------------|
| -quiet  | Suppresses full display of certificate information. Optional.        |
| -nologo | Runs without displaying standard Microsoft copyright data. Optional. |



 

## Related topics

<dl> <dt>

[Side-by-Side Assembly Development Tools](side-by-side-assembly-development-tools.md)
</dt> </dl>

 

 



