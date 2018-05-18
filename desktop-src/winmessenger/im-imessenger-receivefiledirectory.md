---
title: IMessenger ReceiveFileDirectory property
description: Retrieves the local path to the directory currently being used to store any files received through file transfer.
ms.assetid: 'c47a2cdc-7553-4424-a2aa-67ea29611c87'
keywords: ["ReceiveFileDirectory property Windows Messenger", "ReceiveFileDirectory property Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , ReceiveFileDirectory property"]
topic_type:
- apiref
api_name:
- IMessenger.ReceiveFileDirectory
- IMessenger.get_ReceiveFileDirectory
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::ReceiveFileDirectory property

\[**ReceiveFileDirectory** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the local path to the directory currently being used to store any files received through file transfer.

This property is read-only.

## Syntax


```C++
HRESULT get_ReceiveFileDirectory(
  [out, retval] BSTR *bstrPath
);
```



## Property value

Return value. Pointer to a **BSTR** that contains the path to the directory being used to write files sent by file transfer.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                                            |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                                               |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | String comparison failed because the system could not allocate enough memory to create a new **BSTR**. <br/> |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be called from script <br/>                                                                           |
| <dl> <dt>PRC\_X\_NULL\_REF\_POINTER</dt> </dl> | *bstrPath*is a **NULL** pointer.<br/>                                                                        |



## Remarks

This value can be changed from the default by a client user option.

> [!Note]  
> This property is not available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**SendFile**](im-imessenger-sendfile.md)
</dt> </dl>

 

 





