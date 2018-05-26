---
Description: Adds a Certificate object to an open certificate store.
ms.assetid: 787b8a41-dcdb-4b5b-a1fd-f5424300361b
title: Store.Add method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Store.Add method

\[The **Add** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](T:System.Security.Cryptography.X509Certificates.X509Store) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **Add** method adds a [**Certificate**](certificate.md) object to an open [*certificate store*](security.c_gly#-security-certificate-store-gly). This method can only be used with a store that has been opened with read/write permission.

## Syntax


```VB
Store.Add( _
  ByVal Certificate _
)
```



## Parameters

<dl> <dt>

*Certificate* \[in\]
</dt> <dd>

Expression that resolves to a [**Certificate**](certificate.md) object to be added to the store.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

> \[!Important\]  
> When this method is called on a system store from a web script, the script needs to access digital certificates on the local computer. If you allow the script to access your digital certificates, the website from which the script is run will also gain access to any personal information stored in the certificates. The first time this method is called from a particular domain, a dialog box is generated in which the user must indicate whether access to the certificates should be allowed.

 

If the store is not open in read/write mode, this method fails. Although this method can be used with memory stores, any changes made to a memory store are not persisted when the store is closed.

If the certificate being added to the store is the same as one that is already there, the **Add** method deletes the existing certificate from the store and then adds the new certificate. The new certificate inherits properties from the existing certificate.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




