---
description: This topic describes how to verify that the system supports a digest method.
ms.assetid: dd1b53cd-66b9-46b3-89ad-ee84b4690e1e
title: Verify the System Supports a Digest Method
ms.topic: article
ms.date: 05/31/2018
---

# Verify the System Supports a Digest Method

This topic describes how to verify that the system supports a digest method.

XPS Digital Signatures use the Crypto API, which provides methods for verifying that the system supports a specific digest method. To use the Crypto API's **CryptXmlEnumAlgorithmInfo** function to enumerate the digest methods that are supported by the system, the caller must provide a callback method and a data structure. The **CryptXmlEnumAlgorithmInfo** function passes the enumeration data back to the caller by way of the callback method.

The data structure used in this example is shown in the following code example and contains the following fields:

| Field                            | Description                                                                                                |
|----------------------------------|------------------------------------------------------------------------------------------------------------|
| **userDigestAlgorithm**          | An **LPWSTR** field that points to the string that contains the URI of the digest algorithm to be checked. |
| **userDigestAlgorithmSupported** | A **Boolean** value that indicates whether the digest algorithm is supported by the certificate.           |



 


```C++
struct DigestMethodData
{
    LPCWSTR userDigestAlgorithm; 
    BOOL    userDigestAlgorithmSupported;
};
```



The Crypto API method that enumerates the digest methods uses a callback method to return data to the caller. **CryptXmlEnumAlgorithmInfo** enumerates the digest methods that are supported by the system, and it calls the callback method for each digest method that it enumerates, until the callback method returns **FALSE** or until all digest methods supported by the system are enumerated. The callback method in this example compares the digest method that is passed in by **CryptXmlEnumAlgorithmInfo** with the digest method provided by the calling method.


```C++
BOOL WINAPI 
EnumDigestMethodCallback (
    __in   const CRYPT_XML_ALGORITHM_INFO *certMethodInfo,
    __inout_opt  void                     *userArg
)
{
    // MAX_ALG_ID_LEN is used to set the maximum length of the 
    // algorithm URI in the string comparison. The URI is not 
    // likely to be longer than 128 characters so a fixed-size
    // buffer is used in this example.
    // To make this function more robust, consider
    // setting this value dynamically.
    static const  size_t MAX_ALG_ID_LEN = 128;
    DigestMethodData   *certificateAlgorithmData = 
        (DigestMethodData*)userArg;

    if (NULL != userArg) {
        // Assign user data to local data structure
        certificateAlgorithmData = (DigestMethodData*)userArg;
    } else {
        // Unable to continue this enumeration without 
        //  data from calling method.
        return FALSE;
    }
    
    // For each algorithm in the enumeration, check to see 
    //  if the URI of the current supported algorithm matches 
    //  the URI passed in userArg.
    int cmpResult = 0;
    cmpResult = wcsncmp( 
        certMethodInfo->wszAlgorithmURI, 
        certificateAlgorithmData->userDigestAlgorithm, 
        MAX_ALG_ID_LEN );

    if ( 0 == cmpResult )
    {
        // This is a match...
        //  set supported value to true
        certificateAlgorithmData->userDigestAlgorithmSupported = TRUE;
        //  ...and return FALSE to stop any further enumeration
        return FALSE;
    } 
    else
    {
        // no match was found
        // return TRUE to continue enumeration
        return TRUE;
    }
}
```



The following code sample wraps the validation functionality into a single method, which returns a **Boolean** value that indicates whether the system supports the digest method.


```C++
BOOL 
SupportsDigestAlgorithm (
    __in LPCWSTR digestMethodToCheck
)
{
    HRESULT  hr = S_OK;

    // Initialize the structure that will hold information about the 
    //  digest method to check
    DigestMethodData  certificateAlgorithmData;

    certificateAlgorithmData.userDigestAlgorithmSupported = FALSE;
    certificateAlgorithmData.userDigestAlgorithm = digestMethodToCheck;

    // Enumerate the algorithms that are supported on the system, 
    //  the callback method compares each supported algorithm to the one
    //  passed in digestMethodToCheck and returns true in the
    //  certificateAlgorithmData.userDigestAlgorithmSupported field if
    //  the provided digest algorithm is supported by system.
    //
    // Note that CRYPT_XML_GROUP_ID_HASH is set to enumerate 
    //  digest methods
    hr = CryptXmlEnumAlgorithmInfo(
        CRYPT_XML_GROUP_ID_HASH,       // NOTE: CRYPT_XML_GROUP_ID_HASH
        CRYPT_XML_FLAG_DISABLE_EXTENSIONS,
        (void*)&certificateAlgorithmData,
        EnumDigestMethodCallback);

    return certificateAlgorithmData.userDigestAlgorithmSupported;
}
```



## Related topics

<dl> <dt>

**Next Steps**
</dt> <dt>

[Load a Certificate from a File](load-a-certificate-from-a-file.md)
</dt> <dt>

[Verify That a Certificate Supports a Signature Method](verify-a-certificate-supports-a-signature-method.md)
</dt> <dt>

[Embed Certificate Chains in a Document](embedding-certificate-trust-chains-in-a-document.md)
</dt> <dt>

**Used in This Example**
</dt> <dt>

**CryptXmlEnumAlgorithmInfo**
</dt> <dt>

**For More Information**
</dt> <dt>

[Cryptography API](/windows/desktop/SecCrypto/cryptography-portal)
</dt> <dt>

[Cryptography Functions](/windows/desktop/SecCrypto/cryptography-functions)
</dt> <dt>

[XPS Digital Signature API Errors](xps-digital-signatures-errors.md)
</dt> <dt>

[XPS Document Errors](xps-document-errors.md)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 
