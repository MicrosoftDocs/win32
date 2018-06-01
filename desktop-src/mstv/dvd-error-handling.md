---
title: DVD Error Handling
description: DVD Error Handling
ms.assetid: eef87bb8-e01f-40e9-a160-c3e9b066f85d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DVD Error Handling

This topic applies to Windows XP Service Pack 1 or later.

Error handling is crucial in DVD applications; most functions are only valid if the disc has enabled specific features or in specific domains. Visual Basic only returns the decimal equivalent of the first sixteen bits of error codes sent by DirectShow or Windows as the **Err.Number** value. The low 8 bits of this value must be parsed out and compared to standard DirectShow, DirectX, or Windows error messages to provide a comprehensive error management scheme.

The following code shows how to parse out the low 8 bits of an error code:


```C++
Private Sub Command1_Click()
   On Error GoTo Command1_Err

   ' Subroutine here...

   Exit Sub
Command1_Err:
   Dim LOWORD As Long
   Dim HIWORD As Long
   ' Parse out Low and high 8 bit values.
   GetHiLoWord Err.Number, LOWORD, HIWORD
   ' Display decimal and hex values.
   MsgBox "Error number " & vbCrLf & "Decimal: " & LOWORD & _
   vbCrLf & "Hex: " & Hex(LOWORD)
   Resume Next
End Sub

Function GetHiLoWord(lparam As Long, LOWORD As Long, HIWORD As Long)
' Parses out low and high 8 bits from 16-bit lparam variable.
   ' This is the LOWORD of lParam:
   LOWORD = lparam And &amp;HFFFF&amp;
   ' This is the HIWORD of lParam:
   HIWORD = lparam \ &amp;H10000 And &amp;HFFFF&amp;
   gethiloword = 1
End Function
```



As part of error trapping, it is important to check for disabled user operations with the [**UOPValid**](https://www.bing.com/search?q=**UOPValid**) method. This method checks to see if the disc has enabled or disabled certain method or property calls. However, it is important to realize that **UOPValid** only checks to see if the DVD author has specifically disabled an action; it does not indicate whether checking the property or performing the method is normally valid at the current time. Error trapping should handle attempts to perform an action not valid for the current domain or time.

An additional source of unexpected errors stems from the fact that the DVD Navigator filter only sends messages every 1/2 second. Therefore, it is possible that domain or UOP changes may have occurred without notification yet being sent. Attempting to perform an action that has been disabled, or in the previous domain, is a common cause of errors that should be trapped.

For more information on error codes, as well as how Visual Basic handles them, see [Error and Success Codes](https://msdn.microsoft.com/library/windows/desktop/dd375623).

## Related topics

<dl> <dt>

[Error and Success Codes](https://msdn.microsoft.com/library/windows/desktop/dd375623)
</dt> <dt>

[**MSVidWebDVD.UOPValid**](https://www.bing.com/search?q=**MSVidWebDVD.UOPValid**)
</dt> </dl>

 

 




