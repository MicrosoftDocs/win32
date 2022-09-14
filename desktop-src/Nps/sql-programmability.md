---
title: SQL Programmability
description: NPS supports SQL Server logging.
ms.assetid: 55152f56-9ca4-4d0b-a0e9-223168dba83f
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# SQL Programmability

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

NPS supports SQL Server logging.

By default, logging is disabled for NPS. To enable it, run the Network Policy Server snap-in (nps.msc), or the Internet Authentication Service snap-in (ias.msc) and follow the instructions on the Accounting page.

## Sample Stored Procedure

> [!Note]  
> A stored procedure in the SQL Server database that is called by NPS must be named **report\_event**, or the NPS SQL Server logging will fail.

 

The following sample creates an NPS database within the SQL Server 2000 database environment and processes XML documents sent by the NPS servers configured to log to this SQL Server.

In this sample, the NAP-specific information, which is available only from NPS servers running on Windows Server 2008 or later, is stored in the MS\_Quarantine\_State column. The stored procedure report\_event retrieves the values for this column from the XML element **'./MS-Quarantine-State'**. The allowed values for the MS\_Quarantine\_State column are 0 (Full Access), 1 (Quarantined), and 2 (Probation).

``` syntax
IF EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'NPSODBC')
    DROP DATABASE [NPSODBC]
GO

CREATE DATABASE [NPSODBC]  ON (NAME = N'NPSODBC_Data', 
                               FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL\data\NPSODBC_Data.MDF' , 
                               SIZE = 1, FILEGROWTH = 10%) 
                       LOG ON (NAME = N'NPSODBC_Log', 
                               FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL\data\NPSODBC_Log.LDF' , 
                               SIZE = 1, FILEGROWTH = 10%)
 COLLATE SQL_Latin1_General_CP1_CI_AS
GO

exec sp_dboption N'NPSODBC', N'autoclose', N'false'
GO

exec sp_dboption N'NPSODBC', N'bulkcopy', N'false'
GO

exec sp_dboption N'NPSODBC', N'trunc. log', N'false'
GO

exec sp_dboption N'NPSODBC', N'torn page detection', N'true'
GO

exec sp_dboption N'NPSODBC', N'read only', N'false'
GO

exec sp_dboption N'NPSODBC', N'dbo use', N'false'
GO

exec sp_dboption N'NPSODBC', N'single', N'false'
GO

exec sp_dboption N'NPSODBC', N'autoshrink', N'false'
GO

exec sp_dboption N'NPSODBC', N'ANSI null default', N'false'
GO

exec sp_dboption N'NPSODBC', N'recursive triggers', N'false'
GO

exec sp_dboption N'NPSODBC', N'ANSI nulls', N'false'
GO

exec sp_dboption N'NPSODBC', N'concat null yields null', N'false'
GO

exec sp_dboption N'NPSODBC', N'cursor close on commit', N'false'
GO

exec sp_dboption N'NPSODBC', N'default to local cursor', N'false'
GO

exec sp_dboption N'NPSODBC', N'quoted identifier', N'false'
GO

exec sp_dboption N'NPSODBC', N'ANSI warnings', N'false'
GO

exec sp_dboption N'NPSODBC', N'auto create statistics', N'true'
GO

exec sp_dboption N'NPSODBC', N'auto update statistics', N'true'
GO

if( ( (@@microsoftversion / power(2, 24) = 8) and (@@microsoftversion & 0xffff >= 724) ) or 
    ( (@@microsoftversion / power(2, 24) = 7) and (@@microsoftversion & 0xffff >= 1082) ) )
    exec sp_dboption N'NPSODBC', N'db chaining', N'false'
GO

use [NPSODBC]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[report_event]') and 
                                              OBJECTPROPERTY(id, N'IsProcedure') = 1)
drop procedure [dbo].[report_event]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[accounting_data]') and 
                                              OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[accounting_data]
GO

if exists (select * from dbo.systypes where name = N'ipaddress')
exec sp_droptype N'ipaddress'
GO

setuser
GO

EXEC sp_addtype N'ipaddress', N'nvarchar (15)', N'not null'
GO

setuser
GO

CREATE TABLE [dbo].[accounting_data] (
    [id] [int] IDENTITY (1, 1) NOT NULL ,
    [timestamp] [datetime] NOT NULL ,
    [Computer_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL ,
    [Packet_Type] [int] NOT NULL ,
    [User_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [F_Q_User_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Called_Station_Id] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Calling_Station_Id] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Callback_Number] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Framed_IP_Address] [ipaddress] NULL ,
    [NAS_Identifier] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [NAS_IP_Address] [ipaddress] NULL ,
    [NAS_Port] [int] NULL ,
    [Client_Vendor] [int] NULL ,
    [Client_IP_Address] [ipaddress] NULL ,
    [Client_Friendly_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Event_Timestamp] [datetime] NULL ,
    [Port_Limit] [int] NULL ,
    [NAS_Port_Type] [int] NULL ,
    [Connect_Info] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Framed_Protocol] [int] NULL ,
    [Service_Type] [int] NULL ,
    [Authentication_Type] [int] NULL ,
    [NP_Policy_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Reason_Code] [int] NULL ,
    [Class] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Session_Timeout] [int] NULL ,
    [Idle_Timeout] [int] NULL ,
    [Termination_Action] [int] NULL ,
    [EAP_Friendly_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Acct_Status_Type] [int] NULL ,
    [Acct_Delay_Time] [int] NULL ,
    [Acct_Input_Octets] [bigint] NULL ,
    [Acct_Output_Octets] [bigint] NULL ,
    [Acct_Session_Id] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Acct_Authentic] [int] NULL ,
    [Acct_Session_Time] [int] NULL ,
    [Acct_Input_Packets] [bigint] NULL ,
    [Acct_Output_Packets] [bigint] NULL ,
    [Acct_Terminate_Cause] [int] NULL ,
    [Acct_Multi_Session_Id] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Acct_Link_Count] [int] NULL ,
    [Acct_Interim_Interval] [int] NULL ,
    [Tunnel_Type] [int] NULL ,
    [Tunnel_Medium_Type] [int] NULL ,
    [Tunnel_Client_Endpoint] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Tunnel_Server_Endpoint] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Acct_Tunnel_Connection] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Tunnel_Pvt_Group_Id] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Tunnel_Assignment_Id] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Tunnel_Preference] [int] NULL ,
    [MS_Acct_Auth_Type] [int] NULL ,
    [MS_Acct_EAP_Type] [int] NULL ,
    [MS_RAS_Version] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [MS_RAS_Vendor] [int] NULL ,
    [MS_CHAP_Error] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [MS_CHAP_Domain] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [MS_MPPE_Encryption_Types] [int] NULL ,
    [MS_MPPE_Encryption_Policy] [int] NULL ,
    [Proxy_Policy_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Provider_Type] [int] NULL ,
    [Provider_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [Remote_Server_Address] [ipaddress] NULL ,
    [MS_RAS_Client_Name] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
    [MS_RAS_Client_Version] [nvarchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
/*
    The following column stores the NAP-specific information, available from NPS starting with Windows Server 2008. 
    The allowed values are: 0 (Full Access), 1 (Quarantined), and 2 (Probation).
*/
    [MS_Quarantine_State] [int] NULL 
) ON [PRIMARY]
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS OFF 
GO

CREATE PROCEDURE dbo.report_event
    @doc ntext
AS

SET NOCOUNT ON

DECLARE @idoc int
EXEC sp_xml_preparedocument @idoc OUTPUT, @doc

/*
    All RADIUS attributes written to the ODBC format logfile are declared here.  
    One additional attribute is added: @record_timestamp.
    The value of @record_timestamp is the UTC time the record was inserted in the database.

    Refer to IAS-Formatted Log Files in Online Help on www.technet.com for information on interpreting these values.
*/

DECLARE @record_timestamp datetime

SET @record_timestamp = GETUTCDATE()

INSERT accounting_data
SELECT
    @record_timestamp,
    Computer_Name,
    Packet_Type,
    [User_Name],
    F_Q_User_Name,
    Called_Station_Id,
    Calling_Station_Id,
    Callback_Number,
    Framed_IP_Address,
    NAS_Identifier,
    NAS_IP_Address,
    NAS_Port,
    Client_Vendor,
    Client_IP_Address,
    Client_Friendly_Name,
    Event_Timestamp,
    Port_Limit,
    NAS_Port_Type,
    Connect_Info,
    Framed_Protocol,
    Service_Type,
    Authentication_Type,
    NP_Policy_Name,
    Reason_Code,
    Class,
    Session_Timeout,
    Idle_Timeout,
    Termination_Action,
    EAP_Friendly_Name,
    Acct_Status_Type,
    Acct_Delay_Time,
    Acct_Input_Octets,
    Acct_Output_Octets,
    Acct_Session_Id,
    Acct_Authentic,
    Acct_Session_Time,
    Acct_Input_Packets,
    Acct_Output_Packets,
    Acct_Terminate_Cause,
    Acct_Multi_Session_Id,
    Acct_Link_Count,
    Acct_Interim_Interval,
    Tunnel_Type,
    Tunnel_Medium_Type,
    Tunnel_Client_Endpoint,
    Tunnel_Server_Endpoint,
    Acct_Tunnel_Connection,
    Tunnel_Pvt_Group_Id,
    Tunnel_Assignment_Id,
    Tunnel_Preference,
    MS_Acct_Auth_Type,
    MS_Acct_EAP_Type,
    MS_RAS_Version,
    MS_RAS_Vendor,
    MS_CHAP_Error,
    MS_CHAP_Domain,
    MS_MPPE_Encryption_Types,
    MS_MPPE_Encryption_Policy,
    Proxy_Policy_Name,
    Provider_Type,
    Provider_Name,
    Remote_Server_Address,
    MS_RAS_Client_Name,
    MS_RAS_Client_Version,
/*
    NAP-specific information, available from NPS starting with Windows Server 2008. 
*/
    MS_Quarantine_State,
	Event_Source,
	Framed_MTU,
	MS_RAS_Correlation_ID,
	MS_Network_Access_Server_Type,
	SAM_Account_Name,
	Fully_Qualifed_User_Name
FROM OPENXML(@idoc, '/Event')
WITH (
    Computer_Name nvarchar(255) './Computer-Name',
    Packet_Type int './Packet-Type',
    [User_Name] nvarchar(255) './User-Name',
    F_Q_User_Name nvarchar(255) './Fully-Qualifed-User-Name',
    Called_Station_Id nvarchar(255) './Called-Station-Id',
    Calling_Station_Id nvarchar(255) './Calling-Station-Id',
    Callback_Number nvarchar(255) './Callback-Number',
    Framed_IP_Address nvarchar(15) './Framed-IP-Address',
    NAS_Identifier nvarchar(255) './NAS-Identifier',
    NAS_IP_Address nvarchar(15) './NAS-IP-Address',
    NAS_Port int './NAS-Port',
    Client_Vendor int './Client-Vendor',
    Client_IP_Address nvarchar(15) './Client-IP-Address',
    Client_Friendly_Name nvarchar(255) './Client-Friendly-Name',
    Event_Timestamp datetime './Event-Timestamp',
    Port_Limit int './Port-Limit',
    NAS_Port_Type int './NAS-Port-Type',
    Connect_Info nvarchar(255) './Connect-Info',
    Framed_Protocol int './Framed-Protocol',
    Service_Type int './Service-Type',
    Authentication_Type int './Authentication-Type',
    NP_Policy_Name nvarchar(255) './NP-Policy-Name',
    Reason_Code int './Reason-Code',
    Class nvarchar(255) './Class',
    Session_Timeout int './Session-Timeout',
    Idle_Timeout int './Idle-Timeout',
    Termination_Action int './Termination-Action',
    EAP_Friendly_Name nvarchar(255) './EAP-Friendly-Name',
    Acct_Status_Type int './Acct-Status-Type',
    Acct_Delay_Time int './Acct-Delay-Time',
    Acct_Input_Octets bigint './Acct-Input-Octets',
    Acct_Output_Octets bigint './Acct-Output-Octets',
    Acct_Session_Id nvarchar(255) './Acct-Session-Id',
    Acct_Authentic int './Acct-Authentic',
    Acct_Session_Time int './Acct-Session-Time',
    Acct_Input_Packets bigint './Acct-Input-Packets',
    Acct_Output_Packets bigint './Acct-Output-Packets',
    Acct_Terminate_Cause int './Acct-Terminate-Cause',
    Acct_Multi_Session_Id nvarchar(255) './Acct-Multi-Session-Id',
    Acct_Link_Count int './Acct-Link-Count',
    Acct_Interim_Interval int './Acct-Interim-Interval',
    Tunnel_Type int './Tunnel-Type',
    Tunnel_Medium_Type int './Tunnel-Medium-Type',
    Tunnel_Client_Endpoint nvarchar(255) './Tunnel-Client-Endpt',
    Tunnel_Server_Endpoint nvarchar(255) './Tunnel-Server-Endpt',
    Acct_Tunnel_Connection nvarchar(255) './Acct-Tunnel-Connection',
    Tunnel_Pvt_Group_Id nvarchar(255) './Tunnel-Pvt-Group-Id',
    Tunnel_Assignment_Id nvarchar(255) './Tunnel-Assignment-Id',
    Tunnel_Preference int './Tunnel-Preference',
    MS_Acct_Auth_Type int './MS-Acct-Auth-Type',
    MS_Acct_EAP_Type int './MS-Acct-EAP-Type',
    MS_RAS_Version nvarchar(255) './MS-RAS-Version',
    MS_RAS_Vendor int './MS-RAS-Vendor',
    MS_CHAP_Error nvarchar(255) './MS-CHAP-Error',
    MS_CHAP_Domain nvarchar(255) './MS-CHAP-Domain',
    MS_MPPE_Encryption_Types int './MS-MPPE-Encryption-Types',
    MS_MPPE_Encryption_Policy int './MS-MPPE-Encryption-Policy',
    Proxy_Policy_Name nvarchar(255) './Proxy-Policy-Name',
    Provider_Type int './Provider-Type',
    Provider_Name nvarchar(255) './Provider-Name',
    Remote_Server_Address nvarchar(15) './Remote-Server-Address',
    MS_RAS_Client_Name nvarchar(255) './MS-RAS-Client-Name',
    MS_RAS_Client_Version nvarchar(255) './MS-RAS-Client-Version',
/*
    NAP-specific information, available from NPS starting with Windows Server 2008. 
*/
    MS_Quarantine_State int './MS-Quarantine-State',
    Event_Source nvarchar(255) './Event-Source',
	Framed_MTU int './Framed-MTU',
	MS_RAS_Correlation_ID nvarchar(255) './MS-RAS-Correlation-ID',
	MS_Network_Access_Server_Type nvarchar(255) './MS-Network-Access-Server-Type',
	SAM_Account_Name nvarchar(255) './SAM-Account-Name',
	Fully_Qualifed_User_Name nvarchar(255) './Fully-Qualifed-User-Name'
   )

EXEC sp_xml_removedocument @idoc

SET NOCOUNT OFF
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO
```

## Related topics

<dl> <dt>

[TechNet: Key concepts for IAS SQL Server logging](/previous-versions/windows/it-pro/windows-server-2003/cc778830(v=ws.10))
</dt> </dl>

 

 