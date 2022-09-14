---
description: ICE17 checks for the situations shown in the example at the end of this topic.
ms.assetid: a1d9a6e9-4d21-4544-a813-dc82e11f5a26
title: ICE17
ms.topic: article
ms.date: 05/31/2018
---

# ICE17

ICE17 checks for the situations shown in the example at the end of this topic.

## Result

ICE17 displays an error or warning message for each of the situations in the example. Samples of such messages are shown in the following table.



| ICE17 error or warning                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PushButton: Button1 of Dialog: MyDialog does not have an event defined in the ControlEvent table. Error <br/>                                                                                                                | There is a [Pushbutton control](pushbutton-control.md) that is not listed in the [ControlEvent table](controlevent-table.md). If ICE17 returns this error on a PushButton for which the **Enable Control** attribute or the **Visible Control** attribute is not set in the Attributes column of the [Control table](control-table.md), check whether the control also has an entry in the [ControlCondition table](controlcondition-table.md). The control can unexpectedly become enabled, or visible, if the value in the Condition column changes to True, Enable, or Show.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| Bitmap: Bitmap1 of Control: Bitmap1 of Dialog: MyDialog is not in the Binary table. Error <br/>                                                                                                                              | There is a [Bitmap control](bitmap-control.md) or [Icon control](icon-control.md), but the corresponding bitmap or icon is not listed in the [Binary table](binary-table.md). Add the bitmap or icon to the Binary table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| RadioButtonGroup: RadioButton1 of Control: RadioButton1 of Dialog: MyDialog is not in the RadioButton table. Warning <br/>                                                                                                   | There is a [RadioButtonGroup control](radiobuttongroup-control.md) with values in the Property column and the Attribute column of the [Control table](control-table.md); the [Indirect](indirect-control-attribute.md) bit is not set in the Attributes column. ICE17 posts a warning because the installer uses the property's value as a foreign key into the RadioButton table, but the value is missing from the primary key of that table. If the [Indirect](indirect-control-attribute.md) bit is set, then the property listed for the control is not used as the property; instead, it is used as the name of the property that is actually used.<br/> This warning can be ignored if the control is created at runtime. For example, the [ListBox control](listbox-control.md) for on the [FilesInUse Dialog](filesinuse-dialog.md) is only created at runtime if there are files in use during the installation.<br/> |
| ListBox: ListBox1 of Control: ListBox1 of Dialog: MyDialog is not in the ListBox table. Warning <br/>                                                                                                                        | There is a [ListBox control](listbox-control.md) with a value in the Property column of the [Control table](control-table.md) and for which the [Indirect](indirect-control-attribute.md) bit is not set in the Attributes column. ICE17 posts a warning because the installer uses the property's value as a foreign key into the [ListBox table](listbox-table.md), but the value is missing from the primary key of that table. If the [Indirect](indirect-control-attribute.md) bit is set, the control changes the value of a property having a name that is the value of the property associated with this control.<br/> This warning can be ignored if the control is created at runtime. For example, the [ListBox control](listbox-control.md) for on the [FilesInUse Dialog](filesinuse-dialog.md) is only created at runtime if there are files in use during the installation.<br/>                                |
| ComboBox: ComboBox1 of Control: ComboBox1 of Dialog: ByDialog is not in the ComboBox table Warning <br/>                                                                                                                     | There is a [ComboBox control](combobox-control.md) with a value in the Property column of the [Control table](control-table.md) and for which the [Indirect](indirect-control-attribute.md) bit is not set in the Attributes column. ICE17 posts a warning because the installer uses the property's value as a foreign key into the [ComboBox table](combobox-table.md), but the value is missing from the primary key of that table. If the [Indirect](indirect-control-attribute.md) bit is set, the control changes the value of a property having a name that is the value of the property associated with this control.<br/> This warning can be ignored if the control is created at runtime. For example, the [ListBox control](listbox-control.md) for on the [FilesInUse Dialog](filesinuse-dialog.md) is only created at runtime if there are files in use during the installation.<br/>                            |
| ListView: ListView1 of Control: ListView1 of Dialog: MyDialog is not in the ListView table. Warning <br/>                                                                                                                    | There is a [ListView control](listview-control.md) with a value in the Property column of the [Control table](control-table.md) and for which the [Indirect](indirect-control-attribute.md) bit is not set in the Attributes column. ICE17 posts a warning because the installer uses the property's value as a foreign key into the [ListView table](listview-table.md), but the value is missing from the primary key of that table. If the [Indirect](indirect-control-attribute.md) bit is set, the control changes the value of a property having a name that is the value of the property associated with this control.<br/> This warning can be ignored if the control is created at runtime. For example, the [ListBox control](listbox-control.md) for on the [FilesInUse Dialog](filesinuse-dialog.md) is only created at runtime if there are files in use during the installation.<br/>                            |
| Bitmap: 'Bitmap2' for Control: 'Button2' of Dialog: 'MyDialog' not found in Binary table Error <br/>                                                                                                                         | There is a [Pushbutton Control](pushbutton-control.md) or [Checkbox Control](checkbox-control.md) for which the Text column of the [Control table](control-table.md) does not contain a foreign key into the record of the [Binary table](binary-table.md) containing the bitmap or icon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Bitmap: 'Bitmap3' for Control: 'RadioButton2' of Dialog: 'MyDialog' not found in Binary table or<br/> Icon: 'Icon1' for Control: 'RadioButton3' of Dialog: 'MyDialog' not found in Binary table<br/> Error <br/> | There is a [RadioButtonGroup control](radiobuttongroup-control.md) for which the Text column of the [RadioButton table](radiobutton-table.md) does not contain a foreign key into the record of the [Binary table](binary-table.md) containing the bitmap or icon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Picture control: 'Button3' of Dialog: 'MyDialog' has both the Icon and Bitmap attributes set Error <br/>                                                                                                                     | There is a [PushButton](pushbutton-control.md), [CheckBox](checkbox-control.md), or [RadioButtonGroup](radiobuttongroup-control.md) control with both the [Icon](icon-control-attribute.md) bit or [Bitmap](bitmap-control-attribute.md) bit set in the Attributes column of the [Control table](control-table.md). You cannot set both attributes together.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |



 

## Example

[Control Table](control-table.md) (partial)



| Dialog\_ | Control      | Type             | Attributes | Property     | Text       |
|----------|--------------|------------------|------------|--------------|------------|
| MyDialog | Button1      | PushButton       | 0          |              | OK         |
| MyDialog | Bitmap1      | Bitmap           | 0          |              | Bitmap1    |
| MyDialog | RadioButton1 | RadioButtonGroup | 0          | RadioButton1 |            |
| MyDialog | ListBox1     | ListBox          | 0          | ListBox1     |            |
| MyDialog | ComboBox1    | ComboBox         | 0          | ComboBox1    |            |
| MyDialog | ListView1    | ListView         | 0          | ListView1    |            |
| MyDialog | Button2      | Pushbutton       | 262144     |              | Bitmap2    |
| MyDialog | RadioButton2 | RadioButtonGroup | 262144     |              | Property2  |
| MyDialog | RadioButton3 | RadioButtonGroup | 524288     |              | Property3  |
| MyDialog | Button3      | Pushbutton       | 786432     |              | Ambiguous1 |



 

[RadioButton Table](radiobutton-table.md) (partial)



| Property\_ | Order | Text    |
|------------|-------|---------|
| Property2  | 1     | Bitmap3 |
| Property3  | 2     | Icon1   |



 

The following tables are empty:

-   [ControlEvent Table](controlevent-table.md)
-   [ListBox Table](listbox-table.md)
-   [ComboBox Table](combobox-table.md)
-   [ListView Table](listview-table.md)
-   [Binary Table](binary-table.md)

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




