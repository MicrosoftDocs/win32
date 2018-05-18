---
title: IDistList SaveChanges method
description: Provides the ability to save changes to the open distribution list object.
ms.assetid: '2b1cb381-8b8b-456e-a139-aa550129f983'
keywords: ["SaveChanges method Windows Address Book", "SaveChanges method Windows Address Book , IDistList interface", "IDistList interface Windows Address Book , SaveChanges method"]
topic_type:
- apiref
api_name:
- IDistList.SaveChanges
api_location:
- Wab32.dll
api_type:
- COM
---

# IDistList::SaveChanges method

Provides the ability to save changes to the open distribution list object.

## Syntax


```C++
HRESULT SaveChanges(
   ULONG ulFlags
);
```



## Parameters

<dl> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the bitmask of flags that control what happens to the object when the SaveChanges method is called. The following flags can be set:

<dt>

<span id="FORCE_SAVE"></span><span id="force_save"></span>

<span id="FORCE_SAVE"></span><span id="force_save"></span>**FORCE\_SAVE**


</dt> <dd>

Writes changes to the object and closes it. Read-write access must have been enabled for the operation to succeed. This flag forces saving only if MAPI\_E\_OBJECT\_CHANGED was returned from a preceding call to SaveChanges. FORCE\_SAVE overrides the previous changes made to the object.

</dd> <dt>

<span id="KEEP_OPEN_READONLY"></span><span id="keep_open_readonly"></span>

<span id="KEEP_OPEN_READONLY"></span><span id="keep_open_readonly"></span>**KEEP\_OPEN\_READONLY**


</dt> <dd>

Indicates that changes are to be committed and that the object is to be kept open for reading. This flag informs the provider that the object should not be modified and that the calling implementation will not call SaveChanges again. If the provider cannot keep the object open for read-only access, the entire call fails, changes are not saved, and the method returns MAPI\_E\_NO\_ACCESS.

</dd> <dt>

<span id="KEEP_OPEN_READWRITE"></span><span id="keep_open_readwrite"></span>

<span id="KEEP_OPEN_READWRITE"></span><span id="keep_open_readwrite"></span>**KEEP\_OPEN\_READWRITE**


</dt> <dd>

Indicates that changes are to be committed and that the object is to be kept open for read-write access. This flag is usually set when the object was initially opened for read-write access. After calling SaveChanges, the client can make further changes to the object if this flag is passed. If the provider cannot keep the object open for read-write access, the entire call fails, changes are not saved, and the method returns MAPI\_E\_NO\_ACCESS.

</dd> <dt>

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>**MAPI\_DEFERRED\_ERRORS**


</dt> <dd>

This flag is not supported by the WAB.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                             | Description                                                                                          |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | The changes were saved successfully.<br/>                                                      |
| <dl> <dt>**MAPI\_E\_NO\_ACCESS**</dt> </dl>      | An attempt was made to perform an operation for which the user does not have permission. <br/> |
| <dl> <dt>**MAPI\_E\_OBJECT\_CHANGED**</dt> </dl> | The object has changed since it was opened.<br/>                                               |
| <dl> <dt>**MAPI\_E\_OBJECT\_DELETED**</dt> </dl> | The object has been deleted since it was opened.<br/>                                          |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





