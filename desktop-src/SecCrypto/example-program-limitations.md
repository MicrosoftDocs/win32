---
Description: Example Program Limitations
ms.assetid: 2f428872-10ba-4059-ab42-f69dce940bed
title: Example Program Limitations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Example Program Limitations

Principles of good programming practice are not always followed in these sample programs in order to provide more concise, more readable code. In particular:

-   Only limited error responses are shown. Working programs should always check returned error codes and perform appropriate actions when an error is encountered.
-   Only limited memory and resource management is done. In working programs, all keys and [*hashes*](security.h_gly#-security-hash-gly) should be destroyed, all allocated memory should be freed, all files should be closed, and all handles should be released. These example programs provide only limited demonstrations of the use of functions that perform these tasks. These example programs perform no memory or resource management tasks in the case of program termination due to errors.

 

 



