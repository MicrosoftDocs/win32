---
title: FILE\_RESTORE\_CALLBACK function pointer
description: Describes a callback function that is used to report the progress status or finished status of the file restoration process.
ms.assetid: 01bf0208-f69b-498e-b76c-170f4917fb17
keywords:
- FILE_RESTORE_CALLBACK function pointer Files
topic_type:
- apiref
api_name:
- FILE_RESTORE_CALLBACK
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FILE\_RESTORE\_CALLBACK function pointer

The **FILE\_RESTORE\_CALLBACK** function describes a callback function that is used to report the progress status or finished status of the file restoration process.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef BOOLEAN ( *FILE_RESTORE_CALLBACK)(
  _In_ FILE_RESTORE_PACKET_TYPE PacketType,
  _In_ ULONG                    PacketLength,
  _In_ PVOID                    PacketData
);
```



## Parameters

<dl> <dt>

*PacketType* \[in\]
</dt> <dd>

The message type that is sent. For more information, see the [**FILE\_RESTORE\_PACKET\_TYPE**](file-restore-packet-type.md) enumeration.

</dd> <dt>

*PacketLength* \[in\]
</dt> <dd>

The length of the information in the packet, in bytes.

</dd> <dt>

*PacketData* \[in\]
</dt> <dd>

The progress status or finished status of the file restoration process.

</dd> </dl>

## Return value

If the callback returns **FALSE**, the file restore operation is canceled.

## Remarks

Note that there is no associated header file for this callback function.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**RestoreFile**](restorefile.md)
</dt> </dl>

 

 





