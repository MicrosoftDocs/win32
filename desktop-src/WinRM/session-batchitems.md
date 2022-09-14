---
title: Session.BatchItems property (WSManDisp.h)
description: Sets and gets the number of items in each enumeration batch.
ms.assetid: 1675ba12-a0c7-4e59-a013-2109780e8afe
ms.tgt_platform: multiple
keywords:
- BatchItems property Windows Remote Management
- BatchItems property Windows Remote Management , Session object
- Session object Windows Remote Management , BatchItems property
topic_type:
- apiref
api_name:
- Session.BatchItems
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Session.BatchItems property

Sets and gets the number of items in each enumeration batch. This value cannot be changed during an enumeration. The resource provider may set a limit.

This property is read/write.

## Syntax


```VB
Session.BatchItems As long
```



## Property value

Specifies the maximum number of elements returned for each underlying network call to the service. The default is 20.

## Remarks

This is an optimization feature that controls how often network calls are made between the client and the server. Currently, it is used only for enumerations. For more information about enumerating resources, see [**Enumerate**](session-enumerate.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**Session**](session.md)
</dt> <dt>

[**Enumerate**](session-enumerate.md)
</dt> <dt>

[**Enumerator.ReadItem**](enumerator-readitem.md)
</dt> </dl>

 

 





