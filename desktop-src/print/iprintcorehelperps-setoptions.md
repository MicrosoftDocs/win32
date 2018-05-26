---
Description: The IPrintCoreHelperPSSetOptions method sets multiple feature-option pairs at the same time.
ms.assetid: ba80f0f5-ecea-41d7-8ddd-58b417e1fbe7
title: IPrintCoreHelperPSSetOptions method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintCoreHelperPS::SetOptions method

The **IPrintCoreHelperPS::SetOptions** method sets multiple feature-option pairs at the same time.

## Syntax


```C++
STDMETHOD  SetOptions(
  [in, optional] PDEVMODE                   pDevmode,
  [in]           DWORD                      cbSize,
  [in]           BOOL                       bResolveConflicts,
  [in]           CONST PRINT_FEATURE_OPTION pFOPairs[],
  [in]           DWORD                      cPairs,
  [out]          PDWORD                     pcPairsWritten,
  [out]          PDWORD                     pdwResult
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in, optional\]
</dt> <dd>

A pointer to a [**DEVMODEW**](display.devmodew) structure. If this pointer is provided, **IPrintCoreHelperPS::SetOptions** should use the DEVMODEW structure that is pointed to by *pDevmode* rather than the default or current DEVMODEW structure. If this method is called from the plug-in provider or from [**IPrintOemPS::DevMode**](iprintoemps-devmode.md), this parameter is required. In most other situations, the parameter should be **NULL**. When the core driver sets *pDevmode* to **NULL**, it modifies its internal state rather than that of the passed-in DEVMODEW structure. This is required during operations such as full UI replacement, where the DEVMODEW structure returned by a DDI, such as [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md), is being serviced by the core driver's UI module.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The size, in bytes, of the DEVMODEW structure that is pointed to by the *pDevmode* parameter.

</dd> <dt>

*bResolveConflicts* \[in\]
</dt> <dd>

A Boolean value that indicates whether **IPrintCoreHelperPS::SetOptions** should resolve conflicts that arise from one or more constraints in the PPD view of the configuration file, as well as constraints for functionality that are implemented by Pscript or the print processor. If **TRUE**, this method should attempt to resolve the conflict. If **FALSE**, this method should not attempt to resolve conflicts.

</dd> <dt>

*pFOPairs\[\]* \[in\]
</dt> <dd>

An array of [**PRINT\_FEATURE\_OPTION**](print-feature-option.md) elements, where each element contains a feature-option pair. Each feature-option pair lists a feature and the option to select for that feature. All settings are applied sequentially. Duplicates are not disallowed, but settings that appear later in the array (that is, at a higher index) override those that appear earlier in the array.

</dd> <dt>

*cPairs* \[in\]
</dt> <dd>

The number of feature-option pairs that are pointed to by the *pFOPairs* parameter.

</dd> <dt>

*pcPairsWritten* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of feature-option pairs that were successfully saved before **IPrintCoreHelperPS::SetOptions** returned or failed. If this method returns successfully, \**pcPairsWritten* will have the same value as *cPairs*. If the method fails, \**pcPairsWritten* can have any value from zero through the value of *cPairs*. This parameter is optional and can be **NULL**.

</dd> <dt>

*pdwResult* \[out\]
</dt> <dd>

A pointer to a variable that receives the status of the conflict resolution. The status can be one of the following values.



| Value                                                  | Meaning                                                                                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SETOPTIONS\_RESULT\_NO\_CONFLICT<br/>            | No constraint that was specified in the PPD view of the configuration file was violated, relative to the new setting.<br/>                                                                                                                 |
| SETOPTIONS\_RESULT\_CONFLICT\_RESOLVED<br/>      | At least one constraint that was specified in the PPD view of the configuration file was violated, and the caller requested that the method should resolve conflicts. This value results in changed settings with conflicts resolved.<br/> |
| SETOPTIONS\_RESULT\_CONFLICT\_NOT\_RESOLVED<br/> | At least one constraint that was specified in the PPD view of the configuration file was violated, and the caller requested that the method should not resolve conflicts. The settings do not change, and conflicts remain.<br/>           |



 

</dd> </dl>

## Return value

**IPrintCoreHelperPS::SetOptions** should return one of the following values.



| Return code                                                                                   | Description                                                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The operation succeeded.<br/>                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One or more of the arguments is invalid, or the feature was not supported.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Memory for the result array could not be allocated.<br/>                        |



 

For other failures, the method should return a standard COM error code.

## Remarks

**IPrintCoreHelperPS::SetOptions** can be used to make multiple settings changes simultaneously and to resolve constraints after all of the selected options have been set. Changes to options are applied sequentially, starting from the beginning of the *pFOPairs* array, so if the same feature appears twice in this array, only the last option for the feature will be selected. Changes to options are not committed unless the *bResolveConflicts* parameter is **TRUE**.

For most scenarios the *bResolveConflicts* parameter should be set to **TRUE**. Set this parameter to **FALSE** if you want to prompt the user to resolve conflicts.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperPS**](iprintcorehelperps-interface.md)
</dt> <dt>

[**IPrintCoreHelperPS::GetOptions**](iprintcorehelperps-getoption.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperPS::SetOptions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





