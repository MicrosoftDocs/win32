---
description: Use this annotation to associate an effect parameter with a UI control in the host environment. This will allow a user to interactively control an effect parameter through the host application.
ms.assetid: 6d0b2450-7d90-4a24-b710-faed26969876
title: UI Annotation
ms.topic: article
ms.date: 05/31/2018
---

# UI Annotation

Use this annotation to associate an effect parameter with a UI control in the host environment. This will allow a user to interactively control an effect parameter through the host application.

DXSAS defines a set of standard controls in terms of the data model and basic behavior that effect authors can expect from host applications. The control annotation is used like this:


```
string SasUiControl = "ControlType";
```



where


```
ControlType
```



is one of the following:



| ControlType | Description                                                                                                                                                                     | Internal Data Type                                                                                 | Control Property Annotations                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| None        | No control should be shown. Note that a control is visible if [SasUiVisible](#sasuivisible) is True and the control type is any type other than None.                           | n/a                                                                                                | n/a                                                                                                          |
| Any         | This implies that no special control is requested. The control presented is the result of application-defined behavior.                                                         | n/a                                                                                                | n/a                                                                                                          |
| ColorPicker | Represent a color value as a color swatch. The value is packed into the XYZ components of the associated vector. The W component of the associated vector is always set to one. | float*N* where *N* is 1 to 4 inclusive.                                                            | [SasUiEnum](#sasuienum)                                                                                      |
| Direction   | A direction vector.                                                                                                                                                             | float*N* where *N* is 2 to 4 inclusive.                                                            | None                                                                                                         |
| FilePicker  | A dialog box that allows the user to browse and select a file.                                                                                                                  | string                                                                                             | None                                                                                                         |
| ListPicker  | A list of string values from which the user can select one entry. The values are generated from the [SasUiEnum](#sasuienum) annotation.                                         | An array of strings along with an integer value containing the index of the selected string value. | [SasUiEnum](#sasuienum)                                                                                      |
| Numeric     | A set of numerical input controls (such as text boxes).                                                                                                                         | float*M*x*N* where *M* and *N* are 1 to 4 inclusive.                                               | [SasUiMin](#sasuimin), [SasUiMax](#sasuimax), [SasUiStride](#sasuistride)                                    |
| Slider      | A set of sliders.                                                                                                                                                               | float*M*x*N* where *M* and *N* are 1 to 4 inclusive                                                | [SasUiMin](#sasuimin), [SasUiMax](#sasuimax), [SasUiSteps](#sasuisteps), [SasUiStepsPower](#sasuistepspower) |
| String      | An text box for editing string content.                                                                                                                                         | string                                                                                             | None                                                                                                         |



 

If the internal data type is not identical to the associated parameter's type, casting will occur when data is transferred from the host application parameter to the effect parameter.

The default is the string "None".

## UI Common Properties

### SasUiDescription

Use this annotation to specify a string to describe a tool. This could be used for UI elements such as tool tips.


```
string SasUiDescription = "descriptive string";
```



For instance:


```
float3 UpNormal
<
  string SasUiDescription = "The normalized up vector";
>;
```



The default is an empty string.

### SasUiLabel

Use this annotation to specify a string to label any UI control.


```
string SasUiLabel = "some label;
```



Here is an example:


```
float3 UpNormal
<
  string SasUiLabel = "Normal that points up.";
>;
```



The default is an empty string.

### SasUiVisible

Use this annotation to specify whether the associated parameter should be displayed to the user.


```
bool SasUiVisible = false;
```



If set to True, the host application should display a UI control for editing the annotated effect parameter. If false, no UI is displayed in the host application.

Here is an example:


```
float3 UpNormal
<
  string SasUiVisible = false;
>;
```



The default is True.

## UI Control Properties

Control property annotations are additional modifiers that help determine how a particular control operates.

### SasUiEnum

This annotation allows you to restrict the range of values for a control. The annotation contains a string of values delimited by commas.

The default is an empty string.

### SasUiMax

This annotation specifies the maximum value of the associated parameter. It can only be associated with a numerically-typed parameter. The maximum value of the parameter will actually be calculated as:


```
MaxValue = min(FLT_MAX, PARAMETER_TYPE_MAX);
```



PARAMETER\_TYPE\_MAX is the maximum value for the type used by the associated parameter. This means that the value of the parameter, taking into account the [SasUiMax](#sasuimax) annotation is calculated as:


```
ParameterValue = min(NewParameterValue, MaxValue);
```



The default value is FLT\_MAX as defined in Math.h.

### SasUiMin

This annotation specifies the minimum value of the associated parameter. It can only be associated with any numerically-typed parameter. The minimum value of the parameter will actually be calculated as:


```
MinValue = max(-FLT_MAX, PARAMETER_TYPE_MIN);
```



PARAMETER\_TYPE\_MIN is the minimum value for the type used by the associated parameter. This means that the value of the parameter, taking into account the [SasUiMin](#sasuimin) annotation is calculated as:


```
ParameterValue = max(NewParameterValue, MinValue);
```



The default value is -FLT\_MAX as defined in Math.h.

### SasUiSteps

This annotation specifies the number of steps that can be used when incrementing or decrementing the associated parameter value. The annotation is only meaningful on a numerically-typed parameter. Zero specifies that the host application will choose a reasonable number of steps.

The default value is 0.

### SasUiStepsPower

This annotation specifies the exponent in the power function, which has the range \[0.0f, 1.0f\]. Host applications must implement the following method when calculating parameter values:


```
ParameterValue = ((SasUiMax - SasUiMin) x pow(UI_VALUE, SasUiStepsPower) + SasUiMin
```



The default value is 1.0f.

### SasUiStride

This annotation specifies the increment that should be used when incrementing or decrementing this value. Unlike [SasUiSteps](#sasuisteps), [SasUiStride](#sasuistride) is useful with a spinner control, for instance, where the data is unbounded and the user would rather increment the parameter value by stride rather than by a pre-defined number of steps. Host applications should increment (or decrement depending on the control behavior) by the value of SasUiStride as follows:


```
ParameterValue = ParameterValue +/- SasUiStride
```



The default value is 1.0f.

## Related topics

<dl> <dt>

[DirectX Standard Annotations and Semantics Reference](dx9-graphics-reference-effects-dxsas.md)
</dt> </dl>

 

 



