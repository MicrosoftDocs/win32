---
title: Restoring an Instance
description: Restoring an Instance
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'df46a3e6-880c-4c76-a4aa-f576fb51c51e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-application-mode'
ms.tgt_platform: multiple
keywords: ["AD LDS examples ADAM , restoring an instance"]
---

# Restoring an Instance

To restore a backup of an AD LDS instance, stop the AD LDS instance using the Services Administrative Tool and then use the Windows interface of Backup to perform the restore operation. If objects in the directory are inadvertently deleted or modified and if those objects are replicated in a configuration set, you must authoritatively restore those objects so that the correct version of the objects are replicated.

**To restore a backup of an AD LDS instance**

1.  After stopping the AD LDS instance, open **Backup**. Click **Start**, point to **All Programs**, point to **Accessories**, point to **System Tools**, and then click **Backup**.
2.  In Backup or Restore Wizard, click the link for **Advanced Mode**.
3.  In Advanced Mode, click the **Restore and Manage Media** tab.
4.  Select the backup file for the instance to restore by clicking its check box.
5.  In **Restore files to**, click **Original location**.
6.  From the **Tools** menu, click **Options**. In the **Restore** tab of Options, click **Always replace the file on my computer**. Click **OK**.
7.  Click **Start Restore**.
8.  When the **Confirm Restore** dialog appears, click **OK**.
9.  When the restore is done, click **Close** in the **Restore Progress** dialog.

After restoring a backup of an AD LDS instance, perform the following steps.

**To perform an authoritative restore of an AD LDS instance**

1.  Open an AD LDS tools command prompt. Click **Start**, point to **All Programs**, point to **AD LDS**, and then click **AD LDS Tools Command Prompt**.
2.  At the command prompt, type "dsdbutil".
3.  At the dsdbutil prompt, type "authoritative restore"
4.  At the authoritative restore prompt, type one of the commands listed in the following table.

The following table lists authoritative restore commands.

| Command                  | Description                                                                                             |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| **restore database**     | Performs authoritative restore of the entire directory database                                         |
| **restore object** *dn*  | Performs authoritative restore of the directory object whose distinguished name is represented by *dn*  |
| **restore subtree** *dn* | Performs authoritative restore of the directory subtree whose distinguished name is represented by *dn* |



 

For more information about restoring an AD LDS instance, see Restore an AD LDS instance in the Active Directory Lightweight Directory Services Help.

## Related topics

<dl> <dt>

[Backing Up an Instance](backing-up-an-instance.md)
</dt> </dl>

 

 




