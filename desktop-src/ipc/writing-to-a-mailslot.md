---
description: How to write to a mailslot. Writing to a mailslot is similar to writing to a standard disk file.
ms.assetid: a69ba953-cd5c-487f-b9e0-dbd6c44b88b8
title: Writing to a Mailslot
ms.topic: article
ms.date: 05/31/2018
---

# Writing to a Mailslot

Writing to a mailslot is similar to writing to a standard disk file. The following code uses the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea), [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), and [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) functions to put a short message in a mailslot. The message is broadcast to the mailslot server named "sample\_mailslot" on the local computer. The code operates under the assumption that the mailslot server was already created.


```C++
#include <windows.h>
#include <stdio.h>

LPCTSTR SlotName = TEXT("\\\\.\\mailslot\\sample_mailslot");

BOOL WriteSlot(HANDLE hSlot, LPCTSTR lpszMessage)
{
   BOOL fResult; 
   DWORD cbWritten; 
 
   fResult = WriteFile(hSlot, 
     lpszMessage, 
     (DWORD) (lstrlen(lpszMessage)+1)*sizeof(TCHAR),  
     &cbWritten, 
     (LPOVERLAPPED) NULL); 
 
   if (!fResult) 
   { 
      printf("WriteFile failed with %d.\n", GetLastError()); 
      return FALSE; 
   } 
 
   printf("Slot written to successfully.\n"); 

   return TRUE;
}

int main()
{ 
   HANDLE hFile; 

   hFile = CreateFile(SlotName, 
     GENERIC_WRITE, 
     FILE_SHARE_READ,
     (LPSECURITY_ATTRIBUTES) NULL, 
     OPEN_EXISTING, 
     FILE_ATTRIBUTE_NORMAL, 
     (HANDLE) NULL); 
 
   if (hFile == INVALID_HANDLE_VALUE) 
   { 
      printf("CreateFile failed with %d.\n", GetLastError()); 
      return FALSE; 
   } 
 
   WriteSlot(hFile, TEXT("Message one for mailslot."));
   WriteSlot(hFile, TEXT("Message two for mailslot."));

   Sleep(5000);

   WriteSlot(hFile, TEXT("Message three for mailslot."));
 
   CloseHandle(hFile); 
 
   return TRUE;
}
```



The following is the output that is displayed when this example is run with the mailslot server shown in [Reading from a Mailslot](reading-from-a-mailslot.md).

``` syntax
Slot written to successfully.
Slot written to successfully.
Slot written to successfully.
```

 

 
