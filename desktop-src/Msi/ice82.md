---
description: ICE82 validates that the RegisterProduct Action, RegisterUser Action, PublishProduct Action, and PublishFeatures Action are all present in the InstallExecuteSequence table. The package is validated if all the actions are present.
ms.assetid: b41a56f9-b57e-4133-ae7d-c51b36bab44f
title: ICE82
ms.topic: article
ms.date: 05/31/2018
---

# ICE82

ICE82 validates that the [RegisterProduct Action](registerproduct-action.md), [RegisterUser Action](registeruser-action.md), [PublishProduct Action](publishproduct-action.md), and [PublishFeatures Action](publishfeatures-action.md) are all present in the [InstallExecuteSequence table](installexecutesequence-table.md). The package is validated if all the actions are present.

ICE82 posts a warning if there are two actions with the same sequence number listed in the InstallExecuteSequence, InstallUISequence, AdminExecuteSequence, AdminUISequence, or AdvtExecuteSequence tables .

## Result

ICE82 posts the following warnings.



| ICE82 warning                                                                                                                                                                                                                 | Description                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The InstallExecuteSequence table does not contain the set of actions mentioned below: Actions Missing:<br/> Publish Features<br/> Publish Product<br/> Register Product<br/> Register User<br/> | ICE82 custom action posts a warning if all four actions are absent.                                                                                                                                         |
| This action \[1\] has duplicate sequence number \[2\] in the table \[3\].                                                                                                                                                     | ICE82 posts a warning if there are two actions with the same sequence number listed in the InstallExecuteSequence, InstallUISequence, AdminExecuteSequence, AdminUISequence, or AdvtExecuteSequence tables. |



 

ICE82 posts the following errors.



| ICE82 error                                                                                                                                                                                                                                        | Description                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| The InstallExecuteSequence should either contain all of the actions mentioned below or none of them Actions Present<br/> <List of actions present> <br/> Actions Missing:<br/> <List of actions missing> <br/> | ICE82 posts an error if some of the four actions are present and others are absent. |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




