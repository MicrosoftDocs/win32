---
Description: When the Windows Media Audio encoder enumerates output types, it identifies each enumerated type as either Standard, Professional, or Lossless.
ms.assetid: 1c3d22c3-10f7-454a-b1c1-372d684b6568
title: Configuring Standard, Professional, or Lossless Audio Encoding
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring Standard, Professional, or Lossless Audio Encoding

When the Windows Media Audio encoder enumerates output types, it identifies each enumerated type as either Standard, Professional, or Lossless. You can determine whether an output type is Standard, Professional, or Lossless by performing the following steps.

1.  Call [**IMFTransform::GetOutputAvailableType**](/windows/win32/mftransform/nf-mftransform-imftransform-getoutputavailabletype?branch=master) to obtain an [**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master) interface that represents the output type.
2.  Call [**IMFMediaType::GetRepresentation**](/windows/win32/mfobjects/nf-mfobjects-imfmediatype-getrepresentation?branch=master) to get an [**AM\_MEDIA\_TYPE**](dshow.am_media_type) structure that contains information about the output type.
3.  The **pbFormat** member of the [**AM\_MEDIA\_TYPE**](dshow.am_media_type) structure points to a [**WAVEFORMATEX**](dshow.waveformatex) structure that contains additional information about the output type. Inspect the **wFormatTag** member of the **WAVEFORMATEX** structure. A value of 0x161 indicates Standard, a value of 0x162 indicates Professional, and a value of 0x163 indicates Lossless.

If you set properties on the Windows Media Audio encoder before you enumerate output types, you can limit the number of output types that are enumerated. For example, if you set the VBR properties appropriately, you can limit the enumerated output types to those that are in the Lossless category.

## Standard Audio Encoding

You can use the following steps to configure Standard audio encoding.

1.  Set the properties of your choice on the encoder.
2.  Enumerate the possible output types.
3.  Inspect the enumerated types and choose one that has an audio format tag of 0x161.
4.  Set the output type to your chosen type by calling [**IMFTransform::SetOutputType**](/windows/win32/mftransform/nf-mftransform-imftransform-setoutputtype?branch=master).

## Professional Audio Encoding

You can use the following steps to configure Professional audio encoding.

1.  Set the properties of your choice on the encoder.
2.  Enumerate the possible output types.
3.  Inspect the enumerated types and choose one that has an audio format tag of 0x162.
4.  Set the output type to your chosen type by calling [**IMFTransform::SetOutputType**](/windows/win32/mftransform/nf-mftransform-imftransform-setoutputtype?branch=master).

## Lossless Audio Encoding

You can use the following steps to configure Lossless audio encoding.

1.  Set the [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) property to **VARIANT\_TRUE**.
2.  Set the [**MFPKEY\_CONSTRAIN\_ENUMERATED\_VBRQUALITY**](mfpkey-constrain-enumerated-vbrqualityproperty.md) property to **VARIANT\_TRUE**.
3.  Set the [**MFPKEY\_DESIRED\_VBRQUALITY**](mfpkey-desired-vbrqualityproperty.md) property to 100.
4.  Enumerate output types.
5.  Set the output type to one of the types enumerated in step 4 by calling [**IMFTransform::SetOutputType**](/windows/win32/mftransform/nf-mftransform-imftransform-setoutputtype?branch=master).

The following code enumerates all of the lossless output types for the Windows Media Audio encoder. The code prints the value of the audio format tag for each enumerated type. Because all of the enumerated types are lossless, all of those format tags have a value of 0x163. Assume that pIMT is a pointer to an [**IMFTransform**](/windows/win32/mftransform/nn-mftransform-imftransform?branch=master) interface on a Windows Media Audio encoder object and that pStore is a pointer to an **IPropertyStore** interface on the same object. Also assume that hr is a variable of type **HRESULT** that was declared previously in the code.


```
PROPVARIANT prop;
prop.vt = VT_BOOL;
prop.boolVal = VARIANT_TRUE;
hr = pStore->SetValue(MFPKEY_VBRENABLED, prop);

if(SUCCEEDED(hr))
{
   hr = pStore->SetValue(MFPKEY_CONSTRAIN_ENUMERATED_VBRQUALITY, prop);

   if(SUCCEEDED(hr))
   {
      prop.vt = VT_UI4;
      prop.ulVal = 100;
      hr = pStore->SetValue(MFPKEY_DESIRED_VBRQUALITY, prop);
      
      if(SUCCEEDED(hr))
      {           
         HRESULT hrAvailableType = S_OK;
         LONG j = 0;
         while(MF_E_NO_MORE_TYPES != hrAvailableType)
         {
            IMFMediaType* pOutputType = NULL;     
            hrAvailableType = pIMFT->GetOutputAvailableType(
               0, j, &amp;pOutputType);

            if(SUCCEEDED(hrAvailableType))
            {
               AM_MEDIA_TYPE* pTypeRep = NULL;
               hr = pOutputType->GetRepresentation(
                  AM_MEDIA_TYPE_REPRESENTATION, (VOID**)&amp;pTypeRep); 
                     
               if(SUCCEEDED(hr))
               {
                  WAVEFORMATEX* pwfex = (WAVEFORMATEX*)pTypeRep->pbFormat;
                  printf_s("%x\n", pwfex->wFormatTag);
                  pOutputType->FreeRepresentation(
                     AM_MEDIA_TYPE_REPRESENTATION, (VOID*)pTypeRep);
               }

               pOutputType->Release();
               ++j;
            }                                                                  
         } // while                 
      }                                
   } 
}
```



## Related topics

<dl> <dt>

[Configuring Audio Encoding](configuringaudioencoding.md)
</dt> </dl>

 

 



