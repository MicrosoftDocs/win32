---
title: CommonDialog.ShowSelectItems method
description: Displays a dialog box that enables the user to select an Item for transfer from a hardware device for image acquisition.
ms.assetid: 'c02f6143-2bff-4a42-81f7-e2295604a1ee'
keywords: ["ShowSelectItems method WIA Automation", "ShowSelectItems method WIA Automation , CommonDialog object", "CommonDialog object WIA Automation , ShowSelectItems method"]
topic_type:
- apiref
api_name:
- CommonDialog.ShowSelectItems
api_location:
- Wiaaut.h
api_type:
- COM
---

# CommonDialog.ShowSelectItems method

Displays a dialog box that enables the user to select an [**Item**](-wiaaut-item.md) for transfer from a hardware device for image acquisition.

## Syntax


```VB
ppResult = .ShowSelectItems( _
  ByVal Device As Device, _
  [ ByVal Intent As WiaImageIntent ], _
  [ ByVal Bias As WiaImageBias ], _
  [ ByVal SingleSelect As VARIANT_BOOL ], _
  [ ByVal UseCommonUI As VARIANT_BOOL ], _
  [ ByVal CancelError As VARIANT_BOOL ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*Device* \[in\]
</dt> <dd>

Type: **[**Device**](-wiaaut-device.md)\***

Required. [**Device**](-wiaaut-device.md) value.

</dd> <dt>

*Intent* \[in, optional\]
</dt> <dd>

Type: **[**WiaImageIntent**](-wiaaut-wiaimageintent.md)**

[**WiaImageIntent**](-wiaaut-wiaimageintent.md) value.



| Value                                                                                                                                              | Meaning                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt></dt> <dt>UnspecifiedIntent</dt> </dl> | Default. No intent specified.<br/> |



 

</dd> <dt>

*Bias* \[in, optional\]
</dt> <dd>

Type: **[**WiaImageBias**](-wiaaut-wiaimagebias.md)**

[**WiaImageBias**](-wiaaut-wiaimagebias.md) value.



| Value                                                                                                                                            | Meaning                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>MaximizeQuality</dt> </dl> | Default. Use a higher quality scan to maximize the quality of the image.<br/> |



 

</dd> <dt>

*SingleSelect* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether the user must select only one item.



| Value                                                                                                                                  | Meaning                                        |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Multiple selection allowed.<br/>         |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Default. Single selection required.<br/> |



 

</dd> <dt>

*UseCommonUI* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether to use the common UI.



| Value                                                                                                                                  | Meaning                                |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Do not use the common UI.<br/>   |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Default. Use the common UI.<br/> |



 

</dd> <dt>

*CancelError* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether to generate an error if the user cancels the dialog box.



| Value                                                                                                                                  | Meaning                                       |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Default. Do not generate an error.<br/> |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Generate an error.<br/>                 |



 

</dd> </dl>

## Return value

Type: **[**Items**](-wiaaut-items.md)\*\***

Returns the selection as an [**Items**](-wiaaut-items.md) collection on success, otherwise returns **Nothing**.

## Remarks

For example code, see [Count the Number of Child Items Available for Transfer](-wiaaut-shared-samples.md#count-the-number-of-child-items-available-for-transfer) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CommonDialog**](-wiaaut-commondialog.md)
</dt> <dt>

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**ShowAcquisitionWizard**](-wiaaut-icommondialog-showacquisitionwizard.md)
</dt> <dt>

[**ShowDeviceProperties**](-wiaaut-icommondialog-showdeviceproperties.md)
</dt> <dt>

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**Items (Device)**](-wiaaut-idevice-items.md)
</dt> <dt>

[**Connect**](-wiaaut-ideviceinfo-connect.md)
</dt> <dt>

[**Items (Item)**](-wiaaut-iitem-items.md)
</dt> <dt>

[**Items**](-wiaaut-items.md)
</dt> <dt>

[**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md)
</dt> <dt>

[**WiaImageBias**](-wiaaut-wiaimagebias.md)
</dt> <dt>

[**WiaImageIntent**](-wiaaut-wiaimageintent.md)
</dt> </dl>

 

 





