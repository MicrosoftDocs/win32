---
description: The Remove method removes a certificate from an open certificate store. This method can only be used with a store that has been opened with read/write permission.
ms.assetid: 02bb8ff1-2240-4ec7-b8af-9a7812a12ba9
title: Store.Remove method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Remove
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Remove method

\[The **Remove** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/dotnet/api/system.security.cryptography.x509certificates.x509store?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **Remove** method removes a [*certificate*](../secgloss/c-gly.md) from an open [*certificate store*](../secgloss/c-gly.md). This method can only be used with a store that has been opened with read/write permission.

## Syntax


```VB
Store.Remove( _
  ByVal Certificate _
)
```



## Parameters

<dl> <dt>

*Certificate* \[in\]
</dt> <dd>

Expression that resolves to an instance of a [**Certificate**](certificate.md) object to be removed from the store.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

> [!IMPORTANT]
> When this method is called from a web script, the script needs to delete digital certificates from the local computer. Allowing untrusted websites to delete digital certificates is a security risk. A dialog box that asks whether the website can delete certificates appears when this method is first called. If you allow the application to delete certificates and select "Do not show this dialog box again," the dialog box will no longer appear for any script that deletes certificates within that domain. However, scripts outside that domain that attempt to delete certificates will still cause this dialog box to appear. If you do not allow the script to delete certificates and select "Do not show this dialog box again," scripts within that domain will automatically be refused the ability to delete certificates.

 

When you delete a certificate from a store, you should first delete the private key associated with the certificate.

If the store is not open with read/write permission, this method fails. Although this method can be used with memory stores, any changes made to a memory store are not persisted when the store is closed.

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

 

 
