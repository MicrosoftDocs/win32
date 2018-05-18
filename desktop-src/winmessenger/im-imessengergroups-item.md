---
title: IMessengerGroups Item method
description: Retrieves a specific MessengerGroup object by numeric index.
ms.assetid: '1078b9f3-219b-4d57-abed-cbe0e5675275'
keywords: ["Item method Windows Messenger", "Item method Windows Messenger , IMessengerGroups interface", "IMessengerGroups interface Windows Messenger , Item method"]
topic_type:
- apiref
api_name:
- IMessengerGroups.Item
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerGroups::Item method

\[**Item** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a specific [**MessengerGroup**](im-messengergroup.md) object by numeric index.

## Syntax


```C++
HRESULT Item(
  [in]          long      Index,
  [out, retval] IDispatch **ppService
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **long**

**LONG** that specifies the index of the desired [**MessengerGroup**](im-messengergroup.md) object in the collection.

</dd> <dt>

*ppService* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

Address of a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerGroup**](im-messengergroup.md) object requested with **IDispatch** interface on a *Index*. The object can now be accessed through the [**IMessengerGroups**](im-imessengergroups.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                                                  |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success<br/>                                                                           |
| <dl> <dt>**E\_FAIL**</dt> </dl>                    | Invalid collection or index number provided exceeds the length of the collection.<br/> |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl> | *ppMGroup* is a **NULL** pointer.<br/>                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | *Index* is not a positive integer.<br/>                                                |



 

## Remarks

> [!Note]  
> This method is available for scripting languages.

 

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

[**IMessengerGroups**](im-imessengergroups.md)
</dt> </dl>

 

 





