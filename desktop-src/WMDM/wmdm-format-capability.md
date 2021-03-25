---
title: WMDM_FORMAT_CAPABILITY structure
description: The WMDM\_FORMAT\_CAPABILITY structure describes the capabilities of a device for a particular format.
ms.assetid: 9672173D-B11E-4DCB-BCAE-38B94FCC8B99
keywords:
- WMDM_FORMAT_CAPABILITY structure windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_FORMAT_CAPABILITY
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_FORMAT\_CAPABILITY structure

The **WMDM\_FORMAT\_CAPABILITY** structure describes the capabilities of a device for a particular format. This structure contains a set of property configurations in an array of **WMDM\_PROP\_CONFIG** structures. Each property configuration represents a set of compatible property values across all the properties supported for a given format. The application can get this structure by calling the **IWMDMDevice3::GetFormatCapability** method and passing in the format code. For a list of format codes, see [**WMDM\_FORMATCODE**](wmdm-formatcode.md).

## Syntax


```C++
typedef struct _WMDM_FORMAT_CAPABILITY {
  UINT              nPropConfig;
  WMDM_PROP_CONFIG  *pConfigs;
} WMDM_FORMAT_CAPABILITY;
```



## Members

<dl> <dt>

**nPropConfig**
</dt> <dd>

Number of property configurations in the **pConfigs** array.

</dd> <dt>

**pConfigs**
</dt> <dd>

Pointer to an array of [**WMDM\_PROP\_CONFIG**](wmdm-prop-config.md) structures. The size of array is equal to the value of **nPropConfig**.

</dd> </dl>

## Remarks

The **WMDM\_FORMAT\_CAPABILITY** structure provides a flexible mechanism to express the capabilities of the device for a particular format.

If the content is meant to be rendered by the device (for example, an audio file to be played by the device), the properties of the content must match one of the property configurations returned by [**IWMDMDevice3::GetFormatCapability**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getformatcapability) in the **WMDM\_FORMAT\_CAPABILITY** structure. For example, for an audio file, the bit rate and sample rate must satisfy one of the property configurations returned.

The caller is responsible for freeing the memory allocated for this structure. The following function demonstrates how to clear a **WMDM\_FORMAT\_CAPABILITY** structure.


```C++
void FreeFormatCapability(WMDM_FORMAT_CAPABILITY formatCap)
{
    // Loop through all configurations.
    for (UINT i=0; i < formatCap.nPropConfig; i++) 
    {
        // Loop through all descriptions of a configuration and delete
        // the values particular to that description type.
        for (UINT j=0; j < formatCap.pConfigs[i].nPropDesc; j++) 
        {
            switch (formatCap.pConfigs[i].pPropDesc[j].ValidValuesForm)
            {
                case WMDM_ENUM_PROP_VALID_VALUES_ENUM:
                    for (UINT k=0; k < formatCap.pConfigs[i].pPropDesc[j].ValidValues.EnumeratedValidValues.cEnumValues; k++)
                    {
                        PropVariantClear (&(formatCap.pConfigs[i].pPropDesc[j].ValidValues.EnumeratedValidValues.pValues[k]));
                    }
                    CoTaskMemFree(formatCap.pConfigs[i].pPropDesc[j].ValidValues.EnumeratedValidValues.pValues);
                    break;
                case WMDM_ENUM_PROP_VALID_VALUES_RANGE:
                    PropVariantClear (&(formatCap.pConfigs[i].pPropDesc[j].ValidValues.ValidValuesRange.rangeMin));
                    PropVariantClear (&(formatCap.pConfigs[i].pPropDesc[j].ValidValues.ValidValuesRange.rangeMax));
                    PropVariantClear (&(formatCap.pConfigs[i].pPropDesc[j].ValidValues.ValidValuesRange.rangeStep));
                    break;
                case WMDM_ENUM_PROP_VALID_VALUES_ANY:
                    // No dynamically allocated memory for this value.
                default:
                    break;
            }

            // Free the memory for the description name.
            CoTaskMemFree(formatCap.pConfigs[i].pPropDesc[j].pwszPropName);
        }
        // Free the memory holding the array of description items for this configuration.
        CoTaskMemFree(formatCap.pConfigs[i].pPropDesc);
    }

    // Free the memory pointing to the array of configurations.
    CoTaskMemFree(formatCap.pConfigs);
    formatCap.nPropConfig = 0;
}
```



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWMDMDevice3::GetFormatCapability**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getformatcapability)
</dt> <dt>

[**WMDM\_ENUM\_PROP\_VALID\_VALUES\_FORM**](wmdm-enum-prop-valid-values-form.md)
</dt> <dt>

[**WMDM\_PROP\_CONFIG**](wmdm-prop-config.md)
</dt> <dt>

[**WMDM\_PROP\_DESC**](wmdm-prop-desc.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md)
</dt> <dt>

[**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





