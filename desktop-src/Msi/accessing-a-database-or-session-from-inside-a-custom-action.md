---
Description: 'You cannot access an installer session from a custom action that is not the current installation session.'
ms.assetid: '8aa0ac17-1341-4399-987e-d26175150874'
title: Accessing a Database or Session from Inside a Custom Action
---

# Accessing a Database or Session from Inside a Custom Action

You cannot access an installer session from a custom action that is not the current installation session. Custom actions are limited to working with only the active database of the session and no other databases. The following Windows Installer [Database Functions](database-functions.md) must not be called from a custom action, because they require a handle to a database that is not the database of the current installation session:

[**MsiDatabaseMerge**](msidatabasemerge.md)

 

[**MsiCreateTransformSummaryInfo**](msicreatetransformsummaryinfo.md)

 

[**MsiDatabaseApplyTransform**](msidatabaseapplytransform.md)

 

[**MsiDatabaseCommit**](msidatabasecommit.md)

 

[**MsiDatabaseExport**](msidatabaseexport.md)

 

[**MsiDatabaseGenerateTransform**](msidatabasegeneratetransform.md)

 

[**MsiDatabaseImport**](msidatabaseimport.md)

 

[**MsiEnableUIPreview**](msienableuipreview.md)

 

[**MsiGetDatabaseState**](msigetdatabasestate.md)

## Related topics

<dl> <dt>

[Accessing the Current Installer Session from Inside a Custom Action](accessing-the-current-installer-session-from-inside-a-custom-action.md)
</dt> </dl>

 

 



