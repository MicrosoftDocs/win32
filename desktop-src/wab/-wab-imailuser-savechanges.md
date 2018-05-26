---
title: IMailUser SaveChanges method
description: Saves changes to the open mail user object.
ms.assetid: b96a35f0-8b16-43b4-8595-7c2df7b78c82
keywords:
- SaveChanges method Windows Address Book
- SaveChanges method Windows Address Book , IMailUser interface
- IMailUser interface Windows Address Book , SaveChanges method
topic_type:
- apiref
api_name:
- IMailUser.SaveChanges
api_location:
- Wab32.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMailUser::SaveChanges method

Saves changes to the open mail user object.

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

Value of type **ULONG** that specifies the bitmask of flags that control what happens to the object when the **IMailUser::SaveChanges** method is called. The following flags can be set:

<dt>

<span id="FORCE_SAVE"></span><span id="force_save"></span>

<span id="FORCE_SAVE"></span><span id="force_save"></span>**FORCE\_SAVE**


</dt> <dd>

Writes changes to the object and closes it. Read-write access must have been enabled for the operation to succeed. This flag forces saving only if MAPI\_E\_OBJECT\_CHANGED was returned from a preceding SaveChanges call. FORCE\_SAVE overrides the previous changes made to the object.

</dd> <dt>

<span id="KEEP_OPEN_READONLY"></span><span id="keep_open_readonly"></span>

<span id="KEEP_OPEN_READONLY"></span><span id="keep_open_readonly"></span>**KEEP\_OPEN\_READONLY**


</dt> <dd>

Indicates that changes are to be committed and that the object is to be kept open for reading. This flag informs the provider that the object should not be modified and that the calling implementation will not call SaveChanges again. If the provider cannot keep the object open for read-only access, the entire call fails, changes are not saved, and the method returns MAPI\_E\_NO\_ACCESS.

</dd> <dt>

<span id="KEEP_OPEN_READWRITE"></span><span id="keep_open_readwrite"></span>

<span id="KEEP_OPEN_READWRITE"></span><span id="keep_open_readwrite"></span>**KEEP\_OPEN\_READWRITE**


</dt> <dd>

Indicates that changes are to be committed and that the object is to be kept open for read-write access. This flag is usually set when the object was initially opened for read-write access. After calling SaveChanges, the client can make further changes to the object if this flag is passed. If the provider cannot keep the object open for read-write access, the entire call fails, changes are not saved, and the method returns MAPI\_E\_NO\_ACCESS .

</dd> <dt>

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>**MAPI\_DEFERRED\_ERRORS**


</dt> <dd>

Not supported by the WAB.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                             | Description                                                                                          |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | The operation completed successfully.<br/>                                                     |
| <dl> <dt>**MAPI\_E\_NO\_ACCESS**</dt> </dl>      | An attempt was made to perform an operation for which the user does not have permission. <br/> |
| <dl> <dt>**MAPI\_E\_OBJECT\_CHANGED**</dt> </dl> | The object has changed since it was opened.<br/>                                               |
| <dl> <dt>**MAPI\_E\_OBJECT\_DELETED**</dt> </dl> | The object has been deleted since it was opened.<br/>                                          |



 

## Remarks

The following properties may be calculated and changed at **IMailUser::SaveChanges**: PR\_DISPLAY\_NAME, PR\_GIVEN\_NAME, PR\_SURNAME, and PR\_LAST\_MODIFICATION\_TIME.

Calling the **IMailUser::SaveChanges** on an existing WAB entry may fail if the entry was not originally opened with the MAPI\_MODIFY flag.

If KEEP\_OPEN\_READONLY is set and the object cannot be kept open for read-only access, or if KEEP\_OPEN\_READWRITE is set and the object cannot be kept open for read/write access, the method returns MAPI\_E\_NO\_ACCESS.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMailUser**](/windows/previous-versions/wabdefs/?branch=master)
</dt> <dt>

[**OpenEntry**](/windows/previous-versions/Wabiab/?branch=master)
</dt> </dl>

 

 





