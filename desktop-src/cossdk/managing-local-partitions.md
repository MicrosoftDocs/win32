---
description: As an alternative to creating and configuring local partitions through the Component Services administrative tool, you can manage partitions programmatically by using partition-specific COM+ administration collections and properties.
ms.assetid: 82f790cf-3f94-44d9-b722-89a6013d0300
title: Managing Local Partitions
ms.topic: article
ms.date: 05/31/2018
---

# Managing Local Partitions

As an alternative to creating and configuring local partitions through the Component Services administrative tool, you can manage partitions programmatically by using partition-specific COM+ administration collections and properties.

> [!Note]  
> The COM+ partitions service is not enabled by default. To use the COM+ partitions service, you must enable it through the Component Services administration tool or by changing the PartitionsEnabled property on the [**LocalComputer**](localcomputer.md) collection to True.

 

The following subroutine written in Visual Basic script demonstrates how to create a partition on the local computer:


```VB
Sub CreatePartition (PartitonGuid, PartitionName)
   Set cat = CreateObject("COMAdmin.COMAdminCatalog")
   Set collPartitions = cat.GetCollection("Partitions")
   collPartitions.Populate
   Set part = collPartitions.Add
   ' If you don't specify a partition GUID, one is created for you.
   ' Otherwise, you can specify one this way:
   part.Value("ID") = PartitonGuid
   part.Value("Name") = PartitionName
   collPartitions.SaveChanges
   Set part = Nothing
   Set collPartitions = Nothing
   Set cat = Nothing
End Sub 
```



The following subroutine written in Visual Basic script demonstrates how to delete a partition from the local computer:


```VB
Sub DeletePartition (PartitionName)
   Set cat = CreateObject("COMAdmin.COMAdminCatalog")
   Set collPartitions = cat.GetCollection("Partitions")
   collPartitions.Populate
   numPartitions = collPartitions.Count
   ' Begin with the last partition, and work forward through the list.
   For i = numPartitions - 1 To 0 Step -1 
       If collPartitions.Item(i).Value("Name") = PartitionName Then
           collPartitions.Remove i
       End If
   Next
   collPartitions.SaveChanges
   Set collPartitions = Nothing
   Set cat = Nothing
End Sub
```



The following subroutine written in Visual Basic script demonstrates how to set the default partition for a user:


```VB
Sub SetDefaultPartitionForUser(UserName, PartitionGuid)
   Set cat = CreateObject("COMAdmin.COMAdminCatalog")
   Set collUsers = cat.GetCollection("PartitionUsers")
   collUsers.Populate
   Set user = collUsers.Add
   user.Value("AccountName") = UserName
   user.Value("DefaultPartitionID") = PartitionGuid
   collUsers.SaveChanges
   Set collUsers = Nothing
   Set cat = Nothing
End Sub
```



The following subroutine written in Visual Basic script demonstrates how to remove the default partition for a user:


```VB
Sub RemoveDefaultPartitionForUser(UserName)
   Set cat = CreateObject("COMAdmin.COMAdminCatalog")
   Set collUsers = cat.GetCollection("PartitionUsers")
   collUsers.Populate
   numUsers = collUsers.Count
   ' Begin with the last user, and work forward through the list.
   For i = numUsers - 1 To 0 Step -1
       If collUsers.Item(i).Value("AccountName") = UserName Then
           collUsers.Remove i
       End If
   Next
   collUsers.SaveChanges
   Set collUsers = Nothing
   Set cat = Nothing
End Sub
```



## Related topics

<dl> <dt>

[Collecting Partition Metrics](collecting-partition-metrics.md)
</dt> <dt>

[Configuring the Partition Cache](configuring-the-partition-cache.md)
</dt> <dt>

[Grouping Applications into Partitions](grouping-applications-into-partitions.md)
</dt> <dt>

[Managing Partitions Within Active Directory](managing-partitions-within-active-directory.md)
</dt> <dt>

[Setting Administrative Rights for a Partition](setting-administrative-rights-for-a-partition.md)
</dt> </dl>

 

 



