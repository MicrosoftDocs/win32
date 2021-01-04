---
title: IADsNamespaces Property Methods (Iads.h)
description: The IADsNamespaces interface property methods get and set the properties described in the following table. For more information, see Interface Property Methods.
ms.assetid: fe959741-429e-480a-8111-3ebadaf55f77
ms.tgt_platform: multiple
keywords:
- IADsNamespaces Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsNamespaces Property Methods
- IADsNamespaces.DefaultContainer
- IADsNamespaces.get_DefaultContainer
- IADsNamespaces.put_DefaultContainer
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsNamespaces Property Methods

The [**IADsNamespaces**](/windows/desktop/api/Iads/nn-iads-iadsnamespaces) interface property methods get and set the properties described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**DefaultContainer**
</dt> <dd> <dl>

The **DefaultContainer** property identifies a base container object to which you can bind and use as a starting point when browsing. This data is stored and retrieved from the following registry value.

```
HKEY_CURRENT_USER
   Software
      Microsoft
         ADs
            DefaultContainer
```

ADSI defines the **DefaultContainer** property to provide a quick way of getting a pointer to a previously defined ADSI container object.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DefaultContainer(
  [out] BSTR* pbstrDefault
);
HRESULT put_DefaultContainer(
  [in] BSTR bstrDefault
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

Providers must supply this property on a per-user basis. The default container is set immediately after the invocation of **IADsNamespaces::put\_DefaultContainer**. Calling [**IADs.SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) is not required. In fact, the system-supplied namespaces object returns **E\_NOTIMPL** for the **IADs.SetInfo** method called on this object. When a container is the namespaces object, an enumeration operation always results in a list of provider-specific namespace objects. When [**IADsContainer.GetObject**](/windows/desktop/api/Iads/nf-iads-iadscontainer-getobject) is used to obtain a namespace object, the *bstrClass* parameter is ignored. This is because the container, that is, the namespaces object, contains only one type of object, namely, provider-specific namespace objects.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsNamespaces is defined as 28B96BA0-B330-11CF-A9AD-00AA006BC149<br/>       |



## See also

<dl> <dt>

[**IADsContainer.GetObject**](/windows/desktop/api/Iads/nf-iads-iadscontainer-getobject)
</dt> <dt>

[**IADsNamespaces**](/windows/desktop/api/Iads/nn-iads-iadsnamespaces)
</dt> <dt>

[Interface Property Methods](interface-property-methods.md)
</dt> </dl>

 

 





