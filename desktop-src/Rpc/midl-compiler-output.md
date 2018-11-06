---
title: MIDL Compiler Output
description: With the IDL and ACF files as input, the MIDL compiler generates up to five C-language source files.
ms.assetid: 151bd643-1da0-4b33-b8a3-3d7037e63319
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Compiler Output

With the IDL and ACF files as input, the MIDL compiler generates up to five C-language source files. By default, the MIDL compiler uses the base file name of the IDL file as part of the generated stub files. When more than six characters are present in the base file name, some file systems may not accept the full stub name. The following table shows conventions used for file names.



| File        | Default portion of base file name | Example      |
|-------------|-----------------------------------|--------------|
| IDL file    | ---                               | Abcdefgh.idl |
| Header      | .h                                | Abcdef.h     |
| Client stub | \_c.c                             | Abcdef\_c.c  |
| Server stub | \_s.c                             | Abcdef\_s.c  |



 

 

 




