---
description: ICE23 validates the control tab order for each dialog box.
ms.assetid: d425f8c6-4615-439d-8194-3a0325eb3cc3
title: ICE23
ms.topic: article
ms.date: 05/31/2018
---

# ICE23

ICE23 validates the control tab order for each dialog box.

ICE23 validates the following in the [Dialog table](dialog-table.md) and [Control table](control-table.md):

-   That every record in the Dialog table specifies a control in the Control\_First column that exists in the dialog box specified by the Dialog column.
-   That every record in the Control table specifies a control in the Control\_Next column that is on the same dialog as the control listed in the Control column, or Control\_Next contains the Null value.
-   That following the Control\_Next entries from control to control in the Control table makes a single, closed, loop that comes back to the initial control. Not every control needs to be in the loop, but the loop must pass through every control that has an entry in the Control\_Next column.

## Result

ICE23 posts an error message if the tab order of controls does not form a single closed loop in the dialog box.

## Example

ICE23 would post the following error messages for the example shown.

-   Dialog1 has no Control\_First.
-   Control\_First of dialog Dialog2 refers to nonexistent control ControlX.
-   Dialog3 has dead-end tab order at control ControlB.
-   Dialog4 has malformed tab order at control ControlC
-   Dialog5 has malformed tab order at control ControlC.
-   Control\_Next of control Dialog6.ControlC links to unknown control.

[Dialog Table](dialog-table.md) (partial)



| Dialog  | Control\_First |
|---------|----------------|
| Dialog1 |                |
| Dialog2 | ControlX       |
| Dialog3 | ControlA       |
| Dialog4 | ControlA       |
| Dialog5 | ControlA       |



 

[Control Table](control-table.md) (partial)



| Dialog  | Control  | Control\_Next |
|---------|----------|---------------|
| Dialog1 | ControlA |               |
| Dialog1 | ControlB | ControlA      |
| Dialog2 | ControlA | ControlB      |
| Dialog2 | ControlB | ControlA      |
| Dialog3 | ControlA | ControlB      |
| Dialog3 | ControlB |               |
| Dialog4 | ControlA | ControlB      |
| Dialog4 | ControlB | ControlC      |
| Dialog4 | ControlC | ControlB      |
| Dialog5 | ControlA | ControlB      |
| Dialog5 | ControlB | ControlC      |
| Dialog5 | ControlC | ControlA      |
| Dialog5 | ControlD | ControlA      |
| Dialog6 | ControlA | ControlB      |
| Dialog6 | ControlB | ControlC      |
| Dialog6 | ControlC | ControlX      |
| Dialog6 | ControlD | ControlA      |



 

To fix these errors note the following in the above tables and make the indicated changes.

Not every row in the Dialog table has a control specified in the Control\_First column. Change the Control\_First column of the Dialog1 record in the Dialog table to a control that exists in Dialog1.

Not every row in the Dialog table has a control specified in the Control\_First column that exists on the dialog box. Change the Control\_First column of the Dialog2 to a control that exists in Dialog2.

Following the Control\_Next entries in the Control table from control to control does not make a closed loop in every case. Change the Control\_Next column for ControlB in Dialog3 to ControlA.

Following the Control\_Next entries in the Control table from control to control does not lead back to the initial control in every case. Change the Control\_Next column for ControlC in Dialog4 to refer to ControlA.

Following the Control\_Next entries in the Control table from control to control does not pass through every control in the dialog box having an entry in the Control\_Next column. Change the Control\_Next column for ControlC in Dialog5 to ControlD.

Control\_Next does not refer to a valid control that is in the same dialog as the control listed in the Control column. Change the Control\_Next column for ControlC in Dialog6 to refer to ControlD.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



