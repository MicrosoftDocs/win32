---
description: The Import method copies into an open certificate store the contents of a previously exported certificate store. This method can only be used with a store that has been opened with read/write permission.
ms.assetid: 22db8f1c-469b-4baf-9039-4da35c9c6aa0
title: Store.Import method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Import
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Import method

\[The **Import** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/previous-versions/windows/embedded/hh424027(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **Import** method copies into an open [*certificate store*](../secgloss/c-gly.md) the contents of a previously exported certificate store. This method can only be used with a store that has been opened with read/write permission.

## Syntax


```VB
Store.Import( _
  ByVal EncodedStore _
)
```



## Parameters

<dl> <dt>

*EncodedStore* \[in\]
</dt> <dd>

The string that contains the encoded certificates to be imported.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

> [!IMPORTANT]
> When this method is called from a web script, the script needs to access digital certificates on the local computer. If you allow the script to access your digital certificates, the website from which the script is run will also gain access to any personal information stored in the certificates. The first time this method is called from a particular domain, a dialog box is generated in which the user must indicate whether access to the certificates should be allowed.

 

If the store is not opened with read/write permission, this method fails. Although this method can be used with memory stores, any changes made to a memory store are not persisted when the store is closed.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
