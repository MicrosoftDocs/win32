---
title: Generating Four-Character Codes
description: Generating Four-Character Codes
ms.assetid: dfb771f1-9273-4f60-a3af-3a62a3794e59
keywords:
- multimedia file I/O,four-character codes
- file I/O,four-character codes
- input and output (I/O),four-character codes
- I/O (input and output),four-character codes
- four-character codes
- mmioStringToFOURCC function
- mmioFOURCC macro
ms.topic: article
ms.date: 05/31/2018
---

# Generating Four-Character Codes

You can use the [**mmioFOURCC**](https://msdn.microsoft.com/library/Dd757320(v=VS.85).aspx) macro or the [**mmioStringToFOURCC**](https://msdn.microsoft.com/library/Dd757340(v=VS.85).aspx) function to generate four-character codes. The following example uses **mmioFOURCC** to generate a four-character code for "WAVE".


```C++
FOURCC fourccID; 
. 
. 
. 
fourccID = mmioFOURCC('W', 'A', 'V', 'E'); 
 
```



The following example uses [**mmioStringToFOURCC**](https://msdn.microsoft.com/library/Dd757340(v=VS.85).aspx) to generate a four-character code for "WAVE".


```C++
FOURCC fourccID; 
. 
. 
. 
fourccID = mmioStringToFOURCC("WAVE", 0); 
```



The second parameter in [**mmioStringToFOURCC**](https://msdn.microsoft.com/library/Dd757340(v=VS.85).aspx) specifies flags for converting the string to a four-character code. If you specify the MMIO\_TOUPPER flag, **mmioStringToFOURCC** converts all alphabetic characters in the string to uppercase. This is useful when you need to specify a four-character code to identify a custom I/O procedure because four-character codes identifying file-extension names must be all uppercase.

 

 




