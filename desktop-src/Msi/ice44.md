---
description: ICE44 validates that the NewDialog, SpawnDialog, and SpawnWaitDialog ControlEvents reference valid dialog boxes in the Dialog table.
ms.assetid: 401bae25-a361-45f6-af3f-0f31be463c84
title: ICE44
ms.topic: article
ms.date: 05/31/2018
---

# ICE44

ICE44 validates that the [NewDialog](newdialog-controlevent.md), [SpawnDialog](spawndialog-controlevent.md), and [SpawnWaitDialog](spawnwaitdialog-controlevent.md) ControlEvents reference valid dialog boxes in the [Dialog table](dialog-table.md).

## Result

ICE44 posts an error message if there is a dialog control event that does not reference a dialog box listed in the Dialog table.

## Example

ICE44 would report the following errors for the example shown.



| ICE44 error                                                                                                                               | Description                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control Event for Control 'Dialog1'.'Control1' is of type SpawnDialog, but its argument Dialog2 is not a valid entry in the Dialog Table. | There is a SpawnDialog, SpawnWaitDialog, or NewDialog actions that has an argument that does not refer to a dialog box in the Dialog table. To fix this error, add an argument that is a key in the Dialog Table.<br/> |



 

[Dialog Table](dialog-table.md) (partial)



| Dialog  | Title |
|---------|-------|
| Dialog1 |       |



 

[ControlEvent Table](controlevent-table.md) (partial)



| Dialog\_ | Control\_ | Type        | Argument |
|----------|-----------|-------------|----------|
| Dialog1  | Control1  | SpawnDialog | Dialog2  |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




