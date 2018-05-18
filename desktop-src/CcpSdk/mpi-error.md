---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'D66B4D6B-A1FD-461B-BBC0-88742C912B08'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: MPI Error
---

# MPI Error

TBD

<dl> <dt>

<span id="MPI_SUCCESS"></span><span id="mpi_success"></span>**MPI\_SUCCESS**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Successful return code.


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_BUFFER"></span><span id="mpi_err_buffer"></span>**MPI\_ERR\_BUFFER**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Invalid buffer pointer


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_COUNT"></span><span id="mpi_err_count"></span>**MPI\_ERR\_COUNT**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Invalid count argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_TYPE"></span><span id="mpi_err_type"></span>**MPI\_ERR\_TYPE**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



Invalid datatype argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_TAG"></span><span id="mpi_err_tag"></span>**MPI\_ERR\_TAG**
</dt> <dd> <dl> <dt>

4
</dt> <dt>



Invalid tag argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_COMM"></span><span id="mpi_err_comm"></span>**MPI\_ERR\_COMM**
</dt> <dd> <dl> <dt>

5
</dt> <dt>



Invalid communicator


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_RANK"></span><span id="mpi_err_rank"></span>**MPI\_ERR\_RANK**
</dt> <dd> <dl> <dt>

6
</dt> <dt>



Invalid rank


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_ROOT"></span><span id="mpi_err_root"></span>**MPI\_ERR\_ROOT**
</dt> <dd> <dl> <dt>

7
</dt> <dt>



Invalid root


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_GROUP"></span><span id="mpi_err_group"></span>**MPI\_ERR\_GROUP**
</dt> <dd> <dl> <dt>

8
</dt> <dt>



Invalid group


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_OP"></span><span id="mpi_err_op"></span>**MPI\_ERR\_OP**
</dt> <dd> <dl> <dt>

9
</dt> <dt>



Invalid operation


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_TOPOLOGY"></span><span id="mpi_err_topology"></span>**MPI\_ERR\_TOPOLOGY**
</dt> <dd> <dl> <dt>

10
</dt> <dt>



Invalid topology


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_DIMS"></span><span id="mpi_err_dims"></span>**MPI\_ERR\_DIMS**
</dt> <dd> <dl> <dt>

11
</dt> <dt>



Invalid dimension argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_ARG"></span><span id="mpi_err_arg"></span>**MPI\_ERR\_ARG**
</dt> <dd> <dl> <dt>

12
</dt> <dt>



Invalid argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_UNKNOWN"></span><span id="mpi_err_unknown"></span>**MPI\_ERR\_UNKNOWN**
</dt> <dd> <dl> <dt>

13
</dt> <dt>



Unknown error


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_TRUNCATE"></span><span id="mpi_err_truncate"></span>**MPI\_ERR\_TRUNCATE**
</dt> <dd> <dl> <dt>

14
</dt> <dt>



Message truncated on receive


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_OTHER"></span><span id="mpi_err_other"></span>**MPI\_ERR\_OTHER**
</dt> <dd> <dl> <dt>

15
</dt> <dt>



Other error; use Error\_string


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_INTERN"></span><span id="mpi_err_intern"></span>**MPI\_ERR\_INTERN**
</dt> <dd> <dl> <dt>

16
</dt> <dt>



Internal error code


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_IN_STATUS"></span><span id="mpi_err_in_status"></span>**MPI\_ERR\_IN\_STATUS**
</dt> <dd> <dl> <dt>

17
</dt> <dt>



Error code is in status


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_PENDING"></span><span id="mpi_err_pending"></span>**MPI\_ERR\_PENDING**
</dt> <dd> <dl> <dt>

18
</dt> <dt>



Pending request


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_REQUEST"></span><span id="mpi_err_request"></span>**MPI\_ERR\_REQUEST**
</dt> <dd> <dl> <dt>

19
</dt> <dt>



Invalid request (handle)


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_ACCESS"></span><span id="mpi_err_access"></span>**MPI\_ERR\_ACCESS**
</dt> <dd> <dl> <dt>

20
</dt> <dt>



Permission denied


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_AMODE"></span><span id="mpi_err_amode"></span>**MPI\_ERR\_AMODE**
</dt> <dd> <dl> <dt>

21
</dt> <dt>



Error related to amode passed to MPI\_File\_open


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_BAD_FILE"></span><span id="mpi_err_bad_file"></span>**MPI\_ERR\_BAD\_FILE**
</dt> <dd> <dl> <dt>

22
</dt> <dt>



Invalid file name (e.g., path name too long)


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_CONVERSION"></span><span id="mpi_err_conversion"></span>**MPI\_ERR\_CONVERSION**
</dt> <dd> <dl> <dt>

23
</dt> <dt>



Error in user data conversion function


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_DUP_DATAREP"></span><span id="mpi_err_dup_datarep"></span>**MPI\_ERR\_DUP\_DATAREP**
</dt> <dd> <dl> <dt>

24
</dt> <dt>



Data representation identifier already registered


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_FILE_EXISTS"></span><span id="mpi_err_file_exists"></span>**MPI\_ERR\_FILE\_EXISTS**
</dt> <dd> <dl> <dt>

25
</dt> <dt>



File exists


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_FILE_IN_USE"></span><span id="mpi_err_file_in_use"></span>**MPI\_ERR\_FILE\_IN\_USE**
</dt> <dd> <dl> <dt>

26
</dt> <dt>



File operation could not be completed, file in use


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_FILE"></span><span id="mpi_err_file"></span>**MPI\_ERR\_FILE**
</dt> <dd> <dl> <dt>

27
</dt> <dt>



Invalid file handle


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_INFO"></span><span id="mpi_err_info"></span>**MPI\_ERR\_INFO**
</dt> <dd> <dl> <dt>

28
</dt> <dt>



Invalid info argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_INFO_KEY"></span><span id="mpi_err_info_key"></span>**MPI\_ERR\_INFO\_KEY**
</dt> <dd> <dl> <dt>

29
</dt> <dt>



Key longer than MPI\_MAX\_INFO\_KEY


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_INFO_VALUE"></span><span id="mpi_err_info_value"></span>**MPI\_ERR\_INFO\_VALUE**
</dt> <dd> <dl> <dt>

30
</dt> <dt>



Value longer than MPI\_MAX\_INFO\_VAL


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_INFO_NOKEY"></span><span id="mpi_err_info_nokey"></span>**MPI\_ERR\_INFO\_NOKEY**
</dt> <dd> <dl> <dt>

31
</dt> <dt>



Invalid key passed to MPI\_Info\_delete


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_IO"></span><span id="mpi_err_io"></span>**MPI\_ERR\_IO**
</dt> <dd> <dl> <dt>

32
</dt> <dt>



Other I/O error


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_NAME"></span><span id="mpi_err_name"></span>**MPI\_ERR\_NAME**
</dt> <dd> <dl> <dt>

33
</dt> <dt>



Invalid service name in MPI\_Lookup\_name


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_NO_MEM"></span><span id="mpi_err_no_mem"></span>**MPI\_ERR\_NO\_MEM**
</dt> <dd> <dl> <dt>

34
</dt> <dt>



Alloc\_mem could not allocate memory


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_NOT_SAME"></span><span id="mpi_err_not_same"></span>**MPI\_ERR\_NOT\_SAME**
</dt> <dd> <dl> <dt>

35
</dt> <dt>



Collective argument/sequence not the same on all processes


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_NO_SPACE"></span><span id="mpi_err_no_space"></span>**MPI\_ERR\_NO\_SPACE**
</dt> <dd> <dl> <dt>

36
</dt> <dt>



Not enough space


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_NO_SUCH_FILE"></span><span id="mpi_err_no_such_file"></span>**MPI\_ERR\_NO\_SUCH\_FILE**
</dt> <dd> <dl> <dt>

37
</dt> <dt>



File does not exist


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_PORT"></span><span id="mpi_err_port"></span>**MPI\_ERR\_PORT**
</dt> <dd> <dl> <dt>

38
</dt> <dt>



Invalid port name in MPI\_comm\_connect


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_QUOTA"></span><span id="mpi_err_quota"></span>**MPI\_ERR\_QUOTA**
</dt> <dd> <dl> <dt>

39
</dt> <dt>



Quota exceeded


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_READ_ONLY"></span><span id="mpi_err_read_only"></span>**MPI\_ERR\_READ\_ONLY**
</dt> <dd> <dl> <dt>

40
</dt> <dt>



Read-only file or file system


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_SERVICE"></span><span id="mpi_err_service"></span>**MPI\_ERR\_SERVICE**
</dt> <dd> <dl> <dt>

41
</dt> <dt>



Invalid service name in MPI\_Unpublish\_name


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_SPAWN"></span><span id="mpi_err_spawn"></span>**MPI\_ERR\_SPAWN**
</dt> <dd> <dl> <dt>

42
</dt> <dt>



Error in spawning processes


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_UNSUPPORTED_DATAREP"></span><span id="mpi_err_unsupported_datarep"></span>**MPI\_ERR\_UNSUPPORTED\_DATAREP**
</dt> <dd> <dl> <dt>

43
</dt> <dt>



Unsupported dararep in MPI\_File\_set\_view


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_UNSUPPORTED_OPERATION"></span><span id="mpi_err_unsupported_operation"></span>**MPI\_ERR\_UNSUPPORTED\_OPERATION**
</dt> <dd> <dl> <dt>

44
</dt> <dt>



Unsupported operation on file


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_WIN"></span><span id="mpi_err_win"></span>**MPI\_ERR\_WIN**
</dt> <dd> <dl> <dt>

45
</dt> <dt>



Invalid win argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_BASE"></span><span id="mpi_err_base"></span>**MPI\_ERR\_BASE**
</dt> <dd> <dl> <dt>

46
</dt> <dt>



Invalid base passed to MPI\_Free\_mem


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_LOCKTYPE"></span><span id="mpi_err_locktype"></span>**MPI\_ERR\_LOCKTYPE**
</dt> <dd> <dl> <dt>

47
</dt> <dt>



Invalid locktype argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_KEYVAL"></span><span id="mpi_err_keyval"></span>**MPI\_ERR\_KEYVAL**
</dt> <dd> <dl> <dt>

48
</dt> <dt>



Invalid keyval


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_RMA_CONFLICT"></span><span id="mpi_err_rma_conflict"></span>**MPI\_ERR\_RMA\_CONFLICT**
</dt> <dd> <dl> <dt>

49
</dt> <dt>



Conflicting accesses to window


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_RMA_SYNC"></span><span id="mpi_err_rma_sync"></span>**MPI\_ERR\_RMA\_SYNC**
</dt> <dd> <dl> <dt>

50
</dt> <dt>



Wrong synchronization of RMA calls


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_SIZE"></span><span id="mpi_err_size"></span>**MPI\_ERR\_SIZE**
</dt> <dd> <dl> <dt>

51
</dt> <dt>



Invalid size argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_DISP"></span><span id="mpi_err_disp"></span>**MPI\_ERR\_DISP**
</dt> <dd> <dl> <dt>

52
</dt> <dt>



Invalid disp argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_ASSERT"></span><span id="mpi_err_assert"></span>**MPI\_ERR\_ASSERT**
</dt> <dd> <dl> <dt>

53
</dt> <dt>



Invalid assert argument


</dt> </dl> </dd> <dt>

<span id="MPI_ERR_LASTCODE"></span><span id="mpi_err_lastcode"></span>**MPI\_ERR\_LASTCODE**
</dt> <dd> <dl> <dt>

0x3fffffff
</dt> <dt>



Last valid error code for a predefined error class.


</dt> </dl> </dd> </dl>

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |



## See also

<dl> <dt>

[MPI Enumerations](mpi-enumerations.md)
</dt> </dl>

 

 




