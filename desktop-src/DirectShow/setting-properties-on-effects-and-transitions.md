---
description: Setting Properties on Effects and Transitions
ms.assetid: ce773140-7e50-4b72-8cb5-e34cba51644d
title: Setting Properties on Effects and Transitions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting Properties on Effects and Transitions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

Many [DirectShow Editing Services](directshow-editing-services.md) effects and transitions support properties that control their behavior. An application can set the value of a property using the [**IPropertySetter**](ipropertysetter.md) interface. The underlying effect or transition object must support **IDispatch** for setting the properties. With video effects and transitions, the application can set a range of values that change over time. (For example, you can set a wipe transition to move back and forth across the frame.) With audio effects, the value of the property is static and cannot change over time. The only exception is the [Volume Envelope](volume-envelope-effect.md) effect, which supports a dynamic property for the volume level.

To set a property, perform the following steps.

1.  Create an instance of the property setter (CLSID\_PropertySetter).
2.  Fill [**DEXTER\_PARAM**](dexter-param.md) and [**DEXTER\_VALUE**](dexter-value.md) structures with the property data. These structures are discussed below.
3.  Pass the [**DEXTER\_PARAM**](dexter-param.md) and [**DEXTER\_VALUE**](dexter-value.md) structures to the [**IPropertySetter::AddProp**](ipropertysetter-addprop.md) method.
4.  Repeat steps 2 and 3 for each property you want to set.
5.  Pass the [**IPropertySetter**](ipropertysetter.md) interface pointer to the [**IAMTimelineObj::SetPropertySetter**](iamtimelineobj-setpropertysetter.md) method.

The [**DEXTER\_PARAM**](dexter-param.md) structure specifies which property is being set. It contains the following members.

-   **Name**: Name of the property
-   **dispID**: Reserved, must be zero
-   **nValues**: Number of values

The DEXTER\_VALUE structure specifies the value of a property at a given time. It contains the following members.

-   **v**: VARIANT type that specifies a new value for the property. The **vt** member of this VARIANT defines the data type of the property. For more information on the **VARIANT** type, see the Windows SDK.
-   **rt**: Reference time when the property assumes this value, relative to the starting time of the effect or transition. The start time of the effect or transition is relative to the start time of its parent object.
-   **dwInterp**: Flag that specifies how the property changes from the previous value to the new value. With the DEXTERF\_JUMP flag, the property jumps instantly to the new value at the specified time. With the DEXTERF\_INTERPOLATE flag, the property is interpolated linearly from the previous value.

If you set the **vt** member to VT\_BSTR, the property setter makes any necessary conversions. For floating-point values, include the leading zero before the decimal place. For example, 0.3, not .3.

> [!Note]  
> Applications should avoid relying on the conversion from **BSTR**s to numeric values. If the property has a numeric value, use the appropriate numeric **VARIANT** type is possible.

 

The value of a property can change over time, so the [**IPropertySetter::AddProp**](ipropertysetter-addprop.md) method takes a single [**DEXTER\_PARAM**](dexter-param.md) structure and a pointer to an array of [**DEXTER\_VALUE**](dexter-value.md) structures. The array defines a set of time-based values for the property. The members of the array must be in ascending time order, and the **nValues** member of the DEXTER\_PARAM structure must equal the length of the array.

The following code example creates property data for the [SMPTE Wipe](smpte-wipe-transition.md) transition. It sets the wipe code to 120, which creates an oval wipe. It sets the reference time to zero, indicating the start of the transition.


```C++
IPropertySetter     *pProp;   // Property setter
IAMTimelineObj      *pTransObj;  // Transition object
// Create an SMPTE Wipe transition object. (Not shown)

hr = CoCreateInstance(CLSID_PropertySetter, NULL, CLSCTX_INPROC_SERVER,
    IID_IPropertySetter, (void**) &pProp);

// Error checking is omitted for clarity...

DEXTER_PARAM param;
DEXTER_VALUE *pValue = (DEXTER_VALUE*)CoTaskMemAlloc(sizeof(DEXTER_VALUE));

// Initialize the parameter. 
param.Name = SysAllocString(L"MaskNum");
param.dispID = 0;
param.nValues = 1;

// Initialize the value.
pValue->v.vt = VT_I4;
pValue->v.lVal = 120; // Oval
pValue->rt = 0;
pValue->dwInterp = DEXTERF_JUMP;

pProp->AddProp(param, pValue);

// Free allocated resources.
SysFreeString(param.Name);
VariantClear(&(pValue->v));
CoTaskMemFree(pValue);

// Set the property on the transition.
pTransObj->SetPropertySetter(pProp);
pProp->Release();
```



**Dynamically Changing Properties**

After you render a video editing project, it is possible to modify an effect or transition object's properties while the graph is running. However, this is possible only if you set properties on that object before the application called [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md). If so, you can call [**IAMTimelineObj::GetPropertySetter**](iamtimelineobj-getpropertysetter.md) on the effect or transition, clear or modify the properties, and the changes will happen dynamically as the graph is running. There may be visual anomalies while the change occurs, so this is recommended only for preview. Do not change the properties while you are writing the project to a file.

If you did not set any properties on the effect or transition object before you called **ConnectFrontEnd**, you cannot add properties to it while the graph is running.

## Related topics

<dl> <dt>

[Working with Effects and Transitions](working-with-effects-and-transitions.md)
</dt> </dl>

 

 



