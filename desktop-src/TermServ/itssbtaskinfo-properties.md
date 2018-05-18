---
title: ITsSbTaskInfo Properties
description: The ITsSbTaskInfo interface exposes the following properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '402B8502-DE17-440B-867D-45922582C30E'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# ITsSbTaskInfo Properties

The [**ITsSbTaskInfo**](itssbtaskinfo.md) interface exposes the following properties.

## In this section

<dl> <dt>

[**Context property**](itssbtaskinfo-context.md)
</dt> <dd>

Retrieves the context bytes associated with the task.

</dd> <dt>

[**Deadline property**](itssbtaskinfo-deadline.md)
</dt> <dd>

Retrieves the time by which the task must be initiated. This is used to prioritize patches. The patch with the earliest deadline will get initiated first.

</dd> <dt>

[**EndTime property**](itssbtaskinfo-endtime.md)
</dt> <dd>

Retrieves the latest time the task agent can start the task.

</dd> <dt>

[**Identifier property**](itssbtaskinfo-identifier.md)
</dt> <dd>

Retrieves a GUID that is used as a unique identifier by the task agent.

</dd> <dt>

[**Label property**](itssbtaskinfo-label.md)
</dt> <dd>

Retrieves the label that describes the purpose of the task.

</dd> <dt>

[**Plugin property**](itssbtaskinfo-plugin.md)
</dt> <dd>

Retrieves the display name of the task agent.

</dd> <dt>

[**StartTime property**](itssbtaskinfo-starttime.md)
</dt> <dd>

Retrieves the earliest time the task agent can start the task.

</dd> <dt>

[**Status property**](itssbtaskinfo-status.md)
</dt> <dd>

Retrieves an [**RDV\_TASK\_STATUS**](rdv-task-status.md) enumeration value that represents the state of the task.

</dd> <dt>

[**TargetId property**](itssbtaskinfo-targetid.md)
</dt> <dd>

Retrieves the target identifier.

</dd> </dl>

 

 




