---
title: ITsSbTaskInfo Properties
description: The ITsSbTaskInfo interface exposes the following properties.
ms.assetid: 402B8502-DE17-440B-867D-45922582C30E
ms.tgt_platform: multiple
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbTaskInfo Properties

The [**ITsSbTaskInfo**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtaskinfo) interface exposes the following properties.

## In this section

<dl> <dt>

[**Context property**](itssbtaskinfo-context.md)
</dt> <dd>

Retrieves the context bytes associated with the task.

</dd> <dt>

[**Deadline property**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtaskinfo-get_deadline)
</dt> <dd>

Retrieves the time by which the task must be initiated. This is used to prioritize patches. The patch with the earliest deadline will get initiated first.

</dd> <dt>

[**EndTime property**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtaskinfo-get_endtime)
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

[**Plugin property**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtaskinfo-get_plugin)
</dt> <dd>

Retrieves the display name of the task agent.

</dd> <dt>

[**StartTime property**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtaskinfo-get_starttime)
</dt> <dd>

Retrieves the earliest time the task agent can start the task.

</dd> <dt>

[**Status property**](itssbtaskinfo-status.md)
</dt> <dd>

Retrieves an [**RDV\_TASK\_STATUS**](/windows/desktop/api/SessDirPublicTypes/ne-sessdirpublictypes-rdv_task_status) enumeration value that represents the state of the task.

</dd> <dt>

[**TargetId property**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbtaskinfo-get_targetid)
</dt> <dd>

Retrieves the target identifier.

</dd> </dl>

 

 




