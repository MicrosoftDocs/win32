---
description: These escapes are used with the ImmEscape function.
ms.assetid: ede886dc-8a92-428c-8975-3feadc1d4f90
title: IME Escapes
ms.topic: article
ms.date: 05/31/2018
---

# IME Escapes

These escapes are used with the [**ImmEscape**](/windows/desktop/api/Imm/nf-imm-immescapea) function.



| Escape                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IME\_ESC\_GET\_EUDC\_DICTIONARY  | Retrieve the path of the EUDC dictionary file. On input, the *lpData* parameter must be the pointer to the buffer to receive the path. This buffer must be equal to or greater than 80 \* sizeof(TCHAR). On return, the buffer contains the null-terminated string specifying the full path of the dictionary. For use by the Chinese EUDC editor only; do not use in other applications.                                                                                  |
| IME\_ESC\_HANJA\_MODE            | Convert from Hangul to Hanja. On input, *lpData* must point to the buffer that contains the Hangul character to convert; on output, it receives the converted Hanja as a null-terminated string. For use by the Korean editor; do not use in other applications.                                                                                                                                                                                                           |
| IME\_ESC\_IME\_NAME              | Retrieve the name of the IME. On input, the *lpData* parameter must be the pointer to the buffer to receive the name. On return, the buffer contains the null-terminated string specifying the IME name. For use by the Chinese EUDC editor only; do not use in other applications.**Windows Me/98/95:** The buffer must be no less than 16\*sizeof(TCHAR).<br/> **Windows NT, Windows 2000, Windows XP:** The buffer must be no less than 64 characters.<br/> |
| IME\_ESC\_MAX\_KEY               | Return value of the function is the maximum number of key stokes for an EUDC character. For use by the Chinese EUDC editor only; do not use in other applications.                                                                                                                                                                                                                                                                                                         |
| IME\_ESC\_QUERY\_SUPPORT         | Check for implementation. On input, *lpData* points to the buffer that contains the IME Escape value. The function returns 0 if the escape is not implemented.                                                                                                                                                                                                                                                                                                             |
| IME\_ESC\_SEQUENCE\_TO\_INTERNAL | Return the character code that matches the specified sequence code. On input, the *lpData* parameter is the pointer to a 32-bit variable that contains the sequence code. For use by the Chinese EUDC editor only; do not use in other applications. Normally, the Chinese IME will encode its reading character codes into sequence 1 to n.                                                                                                                               |
| IME\_ESC\_SET\_EUDC\_DICTIONARY  | Set the EUDC dictionary file. On input, the *lpData* parameter is the pointer to a null-terminated string specifying the full path. The path should be less than 80 \* sizeof(TCHAR). For use by the Chinese EUDC editor only; do not use in other applications.                                                                                                                                                                                                           |
| IME\_ESC\_GETHELPFILENAME        | **Windows Me/98, Windows 2000, Windows XP:** Return the name of the IME's help file. On return the *lpData* parameter is the full path of the IME's help file. The path should be less than 80 \* sizeof(TCHAR).                                                                                                                                                                                                                                                           |



 

The operating system reserves the escapes in the range IME\_ESC\_RESERVED\_FIRST to IME\_ESC\_RESERVED\_LAST for its own use.

The operating system reserves the escapes in the range IME\_ESC\_PRIVATE\_FIRST to IME\_ESC\_PRIVATE\_LAST for private use by IMEs.

 

 




