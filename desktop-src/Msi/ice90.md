---
description: ICE90 posts a warning if it finds that a shortcut's directory has been specified as a public property.
ms.assetid: 47565d9b-c3c2-4a5c-8f91-2b3912a63b47
title: ICE90
ms.topic: article
ms.date: 05/31/2018
---

# ICE90

ICE90 posts a warning if it finds that a shortcut's directory has been specified as a public property. The names of [Public Properties](public-properties.md) are written in uppercase letters. A shortcut specified by a public property may not work if the value of the [**ALLUSERS**](allusers.md) property changes.

This ICE custom action validates the Shortcut table and uses the Directory table. If the Directory table is not present, it returns without validating the Shortcut table and posts no errors or warnings.

## Result

ICE90 posts the following warning.



| ICE90 error                                                                                                                                                                                                                    | Description                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| The shortcut '\[1\]' has a directory that is a public property (ALL CAPS) and is under user profile directory. This results in a problem if the value of the [**ALLUSERS**](allusers.md) property changes in the UI sequence. | A shortcut's directory has been specified as a public property. |



 

## Example

ICE90 reports the following warning for the example:

``` syntax
The shortcut 'Shortcut1' has a directory that is a public property (ALL CAPS) 
and is under user profile directory. This results in a problem if the value 
of the ALLUSERS property changes in the UI sequence.
```

In this example, MYDIR is under a users profile. ICE90 posts a warning because the location of the target directory is specified by a public property, MYDIR. A user may change MYDIR or [**ALLUSERS**](allusers.md) property. If **ALLUSERS** is set for the per-machine [installation context](installation-context.md), and MYDIR is under a users profile, the shortcut file in MYDIR are copied under the "All Users" profile and not a particular user's profile. If **ALLUSERS** is set for the per-user installation context, the shortcut file in MYDIR is copied into a particular user's profile and is not available to other users.

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Directory\_ |
|-----------|-------------|
| Shortcut1 | MYDIR       |



 

[Directory Table](directory-table.md) (partial)



| Directory | Directory\_Parent |
|-----------|-------------------|
| MYDIR     | ProgramMenuFolder |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



