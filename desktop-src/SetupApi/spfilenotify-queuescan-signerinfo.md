---
description: The SPFILENOTIFY\_QUEUESCAN\_SIGNERINFO notification is sent to a callback routine by SetupScanFileQueue for each node in the copy subqueue of the file queue.
ms.assetid: 5b22e8ba-9a18-461b-bad7-b2d76f83d7f3
title: SPFILENOTIFY_QUEUESCAN_SIGNERINFO message (Setupapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPFILENOTIFY\_QUEUESCAN\_SIGNERINFO message

The **SPFILENOTIFY\_QUEUESCAN\_SIGNERINFO** notification is sent to a callback routine by [**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea) for each node in the copy subqueue of the file queue. This only occurs if the **SetupScanFileQueue** function was called specifying the flag SPQ\_SCAN\_USE\_CALLBACK\_SIGNERINFO. Available starting with Windows XP.


```C++
SPFILENOTIFY_QUEUESCAN_SIGNERINFO
  Param1 = (PFILEPATHS_SIGNERINFO) Filepaths;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS\_SIGNERINFO**](/windows/desktop/api/Setupapi/ns-setupapi-filepaths_signerinfo_a) structure. The **Target** member is the filename of the target file on the system. The **Source** member is the expected path of the source file. The **Win32Error** member is the signing error. Signature information is returned if the callback routine returns **Win32Error**==NO\_ERROR. The **DigitalSigner** member is the digital signer. The **Version** member is the version. The **CatalogFile** is the catalog file.

</dd> </dl>

## Return value

The callback routine should return a [system error code](/windows/desktop/Debug/system-error-codes).

If the callback routine returns NO\_ERROR, the queue scan continues, and returns If the routine returns any other error code, the queue scan aborts and [**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea) returns **FALSE**.

> [!Note]  
> This notification is not handled by the [**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka) function.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Setupapi.h</dt> </dl> |



## See also

<dl> <dt>

[Overview](overview.md)
</dt> <dt>

[Notifications](notifications.md)
</dt> <dt>

[**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea)
</dt> </dl>

 

