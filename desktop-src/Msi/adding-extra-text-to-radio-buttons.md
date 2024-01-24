---
description: Screen reader programs can only read the text of a RadioButtonGroup control that has been authored into the Text column of the RadioButton table.
ms.assetid: 92ad70ec-a3a4-4ea7-8888-40c78d73e58a
title: Adding Extra Text to Radio Buttons
ms.topic: article
ms.date: 05/31/2018
---

# Adding Extra Text to Radio Buttons

Screen reader programs can only read the text of a [RadioButtonGroup control](radiobuttongroup-control.md) that has been authored into the Text column of the [RadioButton table](radiobutton-table.md). If this text is an insufficient description of the radio buttons, overlapping [Text controls](text-control.md) can be added to provide extra descriptive text. These Text controls should overlap each other in the dialog box and have conditions set in the [ControlCondition table](controlcondition-table.md) so that only one Text control is shown at a time. The Text controls must not overlap the RadioButtonGroup control or other controls in the dialog because this makes the controls invisible to screen readers. When the user hovers the cursor over the Text control, the screen reader program reads the extra text.

In the following example the MySample dialog box has a RadioButtonGroup control named Colors with two choices for the value of the TheColor property. For each choice there is a Text control with a condition to hide or show, depending on the current choice selected for TheColor. An initial TheColor value is defined in the Property table. The Text controls have the extra descriptive text authored in the Text field of the RadioButton table. When a user hovers the cursor over the Text control in the dialog box, the screen reader can read the extra description of the current choice.

[Dialog table](dialog-table.md)



| Dialog   | HCentering | VCentering | Width | Height | Attributes | Title                    | Control\_First | Control\_Default | Control\_Cancel |
|----------|------------|------------|-------|--------|------------|--------------------------|----------------|------------------|-----------------|
| MySample | 50         | 50         | 200   | 180    | 3          | Accessible radio buttons | Colors         | Next             |                 |



 

[Control table](control-table.md)



| Dialog\_ | Control    | Type             | X   | Y   | Width | Height | Attributes | Property | Text                               | Control\_Next | Help |
|----------|------------|------------------|-----|-----|-------|--------|------------|----------|------------------------------------|---------------|------|
| MySample | Colors     | RadioButtonGroup | 2   | 20  | 100   | 50     | 3          | TheColor |                                    | Next          |      |
| MySample | HowIsBlue  | Text             | 20  | 80  | 150   | 15     | 2          |          | It is like the sky on a clear day. |               |      |
| MySample | HowIsGreen | Text             | 20  | 80  | 150   | 15     | 2          |          | It is like grass in the spring.    |               |      |



 

[RadioButton table](radiobutton-table.md)



| Property | Order | Value | X   | Y   | Width | Height | Text   | Help |
|----------|-------|-------|-----|-----|-------|--------|--------|------|
| TheColor | 1     | Blue  | 10  | 10  | 80    | 15     | &Blue  |      |
| TheColor | 2     | Green | 10  | 30  | 80    | 15     | &Green |      |



 

[Property table](property-table.md)



| Property | Value |
|----------|-------|
| TheColor | Blue  |



 

[ControlCondition table](controlcondition-table.md)



| Dialog\_ | Control\_  | Action | Condition                 |
|----------|------------|--------|---------------------------|
| MySample | HowIsBlue  | Hide   | TheColor <> "Blue"  |
| MySample | HowIsBlue  | Show   | TheColor = "Blue"         |
| MySample | HowIsGreen | Hide   | TheColor <> "Green" |
| MySample | HowIsGreen | Show   | TheColor = "Green"        |



 

For more information, see [Accessibility](accessibility.md).

 

 



