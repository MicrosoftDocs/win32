---
Description: 'Gets the app suspending operation.'
ms.assetid: '33FCAED5-7568-4483-A643-A536B53F7003'
title: 'ISuspendingEventArgs::SuspendingOperation property'
---

# ISuspendingEventArgs::SuspendingOperation property

Gets the app suspending operation.

This property is read/write.

## Syntax


```C++
HRESULT put_SuspendingOperation();

HRESULT get_SuspendingOperation(
  [out, retval] ISuspendingOperation **value
);
```



## Property value

The suspending operation.

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Windows.ApplicationModel.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.ApplicationModel.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISuspendingEventArgs**](isuspendingeventargs.md)
</dt> </dl>

 

 




