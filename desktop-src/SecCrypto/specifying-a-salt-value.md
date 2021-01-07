---
description: Both the Base Provider and the Extended Provider can specify the value and length of the salt value to be used. The Base Provider sets a salt value using the KP\_SALT parameter value. The Base Provider always sets eleven bytes of salt value.
ms.assetid: ea56d064-b725-431f-b951-66167624e14b
title: Specifying a Salt Value
ms.topic: article
ms.date: 05/31/2018
---

# Specifying a Salt Value

Both the Base Provider and the Extended Provider can specify the value and length of the [*salt value*](../secgloss/s-gly.md) to be used. The Base Provider sets a salt value using the KP\_SALT parameter value. The Base Provider always sets eleven bytes of salt value.

The Enhanced Provider sets the salt value by calling [**CryptSetKeyParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyparam) with the KP\_SALT\_EX parameter value specified and with the *pbData* parameter pointing to a [**CRYPT\_INTEGER\_BLOB**](/previous-versions/windows/desktop/legacy/aa381414(v=vs.85)) structure that contains the salt.

> [!Note]  
> The total length of an Enhanced Provider [*symmetric key*](../secgloss/s-gly.md) and its salt value cannot be greater than 128 bits.

 

KP\_SALT continues to be provided for backward compatibility with the Base Provider. Newer applications should use the KP\_SALT\_EX parameter value.

The following example sets a salt value.


```C++
// Specify 4 bytes of salt.
BYTE rgbSalt[] = {0x01, 0x02, 0x03, 0x04};
CRYPT_DATA_BLOB sSaltData;
sSaltData.pbData = rgbSalt;
sSaltData.cbData = sizeof(rgbSalt);

// Set the 4 bytes of salt required.
// hKey is an HCRYPTPROV handle previously
// assigned, such as by CryptImportKey.
if (CryptSetKeyParam(
        hKey,    
        KP_SALT_EX,    
        (BYTE*)&sSaltData,    
        0))
{
     printf("The salt value is set.\n");
}
else
{
     printf("Setting the salt value failed.\n");
}
```



 

 
