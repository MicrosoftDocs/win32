---
title: Spinner
description: The Spinner is a composite control that consists of an increment button, a decrement button, and an edit control, all of which are used to provide decimal values to the application.
ms.assetid: 63689ed3-7326-4f7a-b700-d89e9b501ef1
ms.topic: article
ms.date: 05/31/2018
---

# Spinner

The Spinner is a composite control that consists of an increment button, a decrement button, and an edit control, all of which are used to provide decimal values to the application.

-   [Details](#details)
-   [Spinner Properties](#spinner-properties)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Details

The following screen shot illustrates the Ribbon Spinner.

![screen shot of a spinner control in the windows live moviemaker ribbon.](images/controls/spinner.png)

## Spinner Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Spinner control.

Typically, a Spinner property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Spinner control.




| Property Key | Notes | 
|--------------|-------|
| <a href="windowsribbon-reference-properties-uipkey-decimalplaces.md">UI_PKEY_DecimalPlaces</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-decimalvalue.md">UI_PKEY_DecimalValue</a> | Supports <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>.<blockquote>[!Note]<br />If the Command associated with the control is invalidated through a call to <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand"><strong>IUIFramework::InvalidateUICommand</strong></a>, the framework queries this property when <code>UI_INVALIDATIONS_VALUE</code> is passed as the value of <em>flags</em>.</blockquote><br /> | 
| <a href="windowsribbon-reference-properties-uipkey-enabled.md">UI_PKEY_Enabled</a> | Supports <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>. | 
| <a href="windowsribbon-reference-properties-uipkey-formatstring.md">UI_PKEY_FormatString</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-increment.md">UI_PKEY_Increment</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-keytip.md">UI_PKEY_Keytip</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-label.md">UI_PKEY_Label</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-largehighcontrastimage.md">UI_PKEY_LargeHighContrastImage</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-largeimage.md">UI_PKEY_LargeImage</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-maxvalue.md">UI_PKEY_MaxValue</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-minvalue.md">UI_PKEY_MinValue</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-representativestring.md">UI_PKEY_RepresentativeString</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-smallhighcontrastimage.md">UI_PKEY_SmallHighContrastImage</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-smallimage.md">UI_PKEY_SmallImage</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-tooltipdescription.md">UI_PKEY_TooltipDescription</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-tooltiptitle.md">UI_PKEY_TooltipTitle</a> | Can only be updated through invalidation. | 




 

The following section of code demonstrates how various properties of the Spinner control are updated in the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) method.


```C++
//
//  FUNCTION:    UpdateProperty()
//
//  PURPOSE:    Called by the Ribbon framework when a command property needs 
//                to be updated.
//
//  COMMENTS:    This function is used to provide new command property values for 
//                the spinner when requested by the Ribbon framework.  
//    
STDMETHODIMP CCommandHandler::UpdateProperty(
    UINT nCmdID,
    REFPROPERTYKEY key,
    const PROPVARIANT* ppropvarCurrentValue,
    PROPVARIANT* ppropvarNewValue)
{
    UNREFERENCED_PARAMETER(ppropvarCurrentValue);

    HRESULT hr = E_NOTIMPL;

    if (nCmdID == IDR_CMD_SPINNER_RESIZE)
    {
        // Set the minimum value
        if (IsEqualPropertyKey(key, UI_PKEY_MinValue))
        {
            ZeroMemory(ppropvarNewValue, sizeof(*ppropvarNewValue));
            ppropvarNewValue->vt = VT_DECIMAL;
            VarDecFromR8(-10.0, &ppropvarNewValue->decVal);
            hr = S_OK;
        }

        // Set the maximum value
        else if (IsEqualPropertyKey(key, UI_PKEY_MaxValue))
        {
            ZeroMemory(ppropvarNewValue, sizeof(*ppropvarNewValue));
            ppropvarNewValue->vt = VT_DECIMAL;
            VarDecFromR8(10.0, &ppropvarNewValue->decVal);
            hr = S_OK;
        }

        // Set the increment
        else if (IsEqualPropertyKey(key, UI_PKEY_Increment))
        {
            ZeroMemory(ppropvarNewValue, sizeof(*ppropvarNewValue));
            ppropvarNewValue->vt = VT_DECIMAL;
            VarDecFromR8(2.0, &ppropvarNewValue->decVal);
            hr = S_OK;
        }

        // Set the number of decimal places
        else if (IsEqualPropertyKey(key, UI_PKEY_DecimalPlaces))
        {
            hr = InitPropVariantFromUInt32(1, ppropvarNewValue);
            hr = S_OK;
        }

        // Set the format string
        else if (IsEqualPropertyKey(key, UI_PKEY_FormatString))
        {
            hr = InitPropVariantFromString(L"px", ppropvarNewValue);
            hr = S_OK;
        }

        // Set the representative string
        else if (IsEqualPropertyKey(key, UI_PKEY_RepresentativeString))
        {
            hr = InitPropVariantFromString(L"AAAAAAA", ppropvarNewValue);
            hr = S_OK;
        }
    }
    return hr;
}
```



## Remarks

If the minimum value ([UI\_PKEY\_MinValue](windowsribbon-reference-properties-uipkey-minvalue.md)) of a Spinner is initialized to 0.0, the application should ensure that any subsequent value supplied by the control does not equal -0.0 (negative zero). If the Spinner supplies a value of -0.0, the application should reset this value to 0.0 (positive zero) using the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method as shown in the following example of an [**IUICommandHandler::Execute**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-execute) method for a Spinner control.

> [!Note]  
> If this test is not performed and the value left uncorrected, the edit field of the control displays the string "Auto".

 


```C++
//
//  FUNCTION:    Execute()
//
//  PURPOSE:    Called by the Ribbon framework when a command is executed by the user.  
//                For this sample, when an increment or decrement button is pressed or
//                a new value is entered in the Spinner edit field.
//
STDMETHODIMP CCommandHandler::Execute(
      UINT nCmdID,
      UI_EXECUTIONVERB verb,
      const PROPERTYKEY* key,
      const PROPVARIANT* ppropvarValue,
      IUISimplePropertySet* pCommandExecutionProperties)
{
    UNREFERENCED_PARAMETER(pCommandExecutionProperties);

    HRESULT hr = E_NOTIMPL;

    if (verb == UI_EXECUTIONVERB_EXECUTE)
    {
        RenderParam param;
        g_renderer.GetRenderParam(&param);

        if (nCmdID == IDR_CMD_SPINNER_RESIZE)
        {
            // Spinner value is negative.
            if (!(ppropvarValue->decVal.sign == 0))
            {
                // Check if the value supplied by the Spinner is -0
                // and correct the value if necessary.
                // If this value is left uncorrected, the edit field 
                // of the control will display the string "Auto" when 
                // UI_PKEY_MinValue is set to 0.
                if (ppropvarValue->decVal.Lo64 == 0)
                {
                    // Initialize a new PROPVARIANT structure.
                    PROPVARIANT m_varNewVal;
                    PropVariantInit(&m_varNewVal);

                    // The replacement DECIMAL value.
                    DECIMAL m_dVal;
                    hr = VarDecFromI4(0, &m_dVal);
                    if (FAILED(hr))
                    {
                        return hr;
                    }
                    
                    // Initialize the new DECIMAL value.
                    UIInitPropertyFromDecimal(UI_PKEY_DecimalValue, m_dVal, &m_varNewVal);

                    // Set the UI_PKEY_DecimalValue to the new DECIMAL value.
                    hr = g_pFramework->SetUICommandProperty(nCmdID, UI_PKEY_DecimalValue, m_varNewVal);
                    if (FAILED(hr))
                    {
                        return hr;
                    }
                }
                // Decrease size of shape in document space.
                param.iShapeSizeIncrement = -ppropvarValue->intVal;
            }
            // Spinner value is positive.
            else
            {
                // Increase size of shape in document space.
                param.iShapeSizeIncrement = ppropvarValue->intVal;
            }
        }
        g_renderer.UpdateRenderParam(param);
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**Spinner markup element**](windowsribbon-element-spinner.md)
</dt> </dl>

