---
description: Specifies the activatable class ID of the Encrypted Media Extension object in the content protection system, represented as a string.
title: MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATABLE_CLASS_ID (mfcontentdecryptionmodule.h)
ms.topic: reference
ms.date: 01/27/2026
---

# MF\_ENCRYPTEDMEDIAEXTENSIONS\_ACTIVATABLE\_CLASS\_ID property

Specifies the activatable class ID of the Encrypted Media Extension object in the content protection system, represented as a string.


## Data type

**LPWSTR** (VT_LPWSTR)

## Property GUID

**MF\_ENCRYPTEDMEDIAEXTENSIONS\_ACTIVATABLE\_CLASS\_ID**

## Property value

A string containing the activatable class ID of the Encrypted Media Extension object in the content protection system.

## Remarks

This property enables apps to instantiate and initialize an Encrypted Media Extension (EME) object in an external process. In this scenario, an app calls [IMFPMPHost::CreateObjectByCLSID method](/windows/win32/api/mfidl/nf-mfidl-imfpmphost-createobjectbyclsid), specifying **MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATE**, which is the CLSID of a proxy object that implements [IMFActivate](/windows/win32/api/mfobjects/nn-mfobjects-imfactivate). An app sets the **MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATABLE_CLASS_ID** property in the creation attributes for **MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATE** proxy. Calls to [ActivateObject](/win32/api/mfobjects/nf-mfobjects-imfactivate-activateobject) on the proxy object specify IID of an interface implemented by the Encrypted Media Extension, such as [IMFTrustedInput](/windows/win32/api/mfidl/nn-mfidl-imftrustedinput). 

## Examples

The following example shows a helper function that could be used by an app to instantiate and initialize an Encrypted Media Extension (EME) object in an external process. This function can be used as part of a larger implementation of the [IMFPMPHostApp::ActivateClassById](/windows/win32/api/mfidl/nf-mfidl-imfpmphostapp-activateclassbyid) method. The helper function uses [IMFPMPHost::CreateObjectByCLSID](IMFPMPHost::CreateObjectByCLSID]) to instantiate the EME object.

```cpp
#include <wil/com.h> 
#include <mfidl.h> 
#include <mfapi.h> 
#include <mfcontentdecryptionmodule.h> 

HRESULT ActivateEncryptedMediaExtensionInExternalProcess( 
    _In_ IMFPMPHost* pmp_host, 
    _In_ PCWSTR activatableClassId, // The "id" parameter in IMFPMPHostApp::ActivateClassById 
    _In_reads_opt_(initializationDataSize) const BYTE* initializationData, 
    size_t initializationDataSize, 
    REFIID riid, 
    _Outptr_ void** activated_class) 
{ 
    wil::com_ptr_nothrow<IMFAttributes> creation_attributes; 
    RETURN_IF_FAILED(MFCreateAttributes(&creation_attributes, 2)); 

    // Specify the Activatable Class ID of the runtime class that implements the Encrypted Media Extension. 
    RETURN_IF_FAILED(creation_attributes->SetString(MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATABLE_CLASS_ID,  
        activatableClassId)); 

    // If initialization data is available, it is also stored in the IMFAttributes property store. 
    // When implementing IMFPMPHostApp::ActivateClassById, the initialization data is read from the 
    // "pStream" parameter of that method. 

    if (initializationData != nullptr) 
    { 
        RETURN_IF_FAILED(creation_attributes->SetBlob(MF_ENCRYPTEDMEDIAEXTENSIONS_INITIALIZATION_DATA,  
            initializationData, initializationDataSize)); 
    } 

    // Serialize the contents of the IMFAttributes property store into an IStream. 
    wil::com_ptr_nothrow<IStream> output_stream; 
    RETURN_IF_FAILED(CreateStreamOnHGlobal(nullptr, TRUE, &output_stream)); 
    RETURN_IF_FAILED(MFSerializeAttributesToStream(creation_attributes.get(), 0, output_stream.get())); 
    RETURN_IF_FAILED(output_stream->Seek({}, STREAM_SEEK_SET, nullptr)); 

    // Create an activator for the Encrypted Media Extension. 
    wil::com_ptr_nothrow<IMFActivate> activator; 
    RETURN_IF_FAILED(pmp_host->CreateObjectByCLSID( 
        MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATE, 
        output_stream.get(), 
        IID_PPV_ARGS(&activator))); 

    // Activate the Encrypted Media Extension. 
    // The riid parameter is for any IID of an interface implemented by the 
    // Encrypted Media Extension, such as IMFTrustedInput. 
    RETURN_IF_FAILED(activator->ActivateObject(riid, activated_class)); 

    return S_OK; 
}  
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 April 2020 Update<br/>                                     |
| Header<br/>                   | <dl> <dt>mfcontentdecryptionmodule.h</dt> </dl> |



## See also

- [Media Foundation Properties](media-foundation-properties.md)
- [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule)


 

 




