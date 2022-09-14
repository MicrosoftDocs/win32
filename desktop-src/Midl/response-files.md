---
title: Response Files
description: As an alternative to placing all the options on the command line, the MIDL compiler accepts response files that contain switches and arguments.
ms.assetid: 53ee9ad2-1ab4-421f-99c9-66186da4bd9d
keywords:
- MIDL compiler MIDL , response files
ms.topic: article
ms.date: 05/31/2018
---

# Response Files

As an alternative to placing all the options on the command line, the MIDL compiler accepts response files that contain switches and arguments. A response file is a text file containing one or more MIDL compiler command-line options. Unlike a command line, a response file allows multiple lines of options and file names. This may be useful due to limitations of your build environment or as a convenience for your build process. You can specify a MIDL response file as:

**midl** **\@filename**

<dl> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Specifies the name of the response file. The response file name must immediately follow the @ character with no white space between the @ character and the response file name.

</dd> </dl>

Options in a response file are interpreted as if they were present at that place in the MIDL command line. Each argument in a response file must begin and end on the same line. You cannot use the backslash character (\\) to concatenate lines.

MIDL supports command-line arguments that include one or more response files, combined with other command-line switches:

**midl -Oicf @midl1.rsp -envwin32 @midl2.rsp itf.idl**

The MIDL compiler does not support nested response files.

 

 




