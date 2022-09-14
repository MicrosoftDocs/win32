---
title: Task Scheduler Schema
description: The Task Scheduler schema defines valid XML used to register tasks with the Task Scheduler service. Developers can create their own XML, validate it against this schema, and register tasks using the ITaskFolder RegisterTask method.
ms.assetid: 9b1b8e34-c635-413a-a230-79a58017cf21
keywords:
- Task Scheduler Task Scheduler , reference, XML schema
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Task Scheduler Schema

The Task Scheduler schema defines valid XML used to register tasks with the Task Scheduler service. Developers can create their own XML, validate it against this schema, and register tasks using the [**ITaskFolder::RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) method.

The types and elements of the Task Scheduler schema are individually documented in the following sections.

-   [Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
-   [Task Scheduler Schema Simple Types](task-scheduler-schema-simple-types.md)
-   [Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
-   [Task Scheduler Schema Groups](task-scheduler-schema-groups.md)

The entire Task Scheduler schema is defined by the following XSD file.


```XML
<?xml version="1.0" encoding="utf-8" ?>
<xs:schema
    targetNamespace="http://schemas.microsoft.com/windows/2004/02/mit/task"
    xmlns:xs="https://www.w3.org/2001/XMLSchema"
    xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"
    xmlns:td="http://schemas.microsoft.com/windows/2004/02/mit/task"
    elementFormDefault="qualified">

    <xs:element name="Task" type="taskType">

        <xs:key name="PrincipalKey">
            <xs:selector xpath="td:Principals/td:Principal" />
            <xs:field xpath="@id" />
        </xs:key>

        <!-- Principal id in Context attribute should match an id of
             some principal in Principals section. -->
        <xs:keyref name="ContextKeyRef" refer="PrincipalKey">
            <xs:selector xpath="td:Actions" />
            <xs:field xpath="@Context" />
        </xs:keyref>

        <!-- All ids must be unique -->
        <xs:unique name="UniqueId">
            <xs:selector xpath="td:Principals/td:Principal|td:Triggers/td:BootTrigger|td:Triggers/td:RegistrationTrigger|td:Triggers/td:IdleTrigger|td:Triggers/td:TimeTrigger|td:Triggers/td:EventTrigger|td:Triggers/td:LogonTrigger|td:Triggers/td:SessionStateChangeTrigger|td:Triggers/td:CalendarTrigger|td:Actions/td:Exec|td:Actions/td:ComHandler|td:Actions/td:SendEmail" />
            <xs:field xpath="@id" />
        </xs:unique>

    </xs:element>

    <xs:simpleType name="nonEmptyString">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
        </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="pathType">
        <xs:restriction base="nonEmptyString">
            <xs:maxLength value="260"/>
        </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="versionType">
        <xs:restriction base="xs:string">
            <xs:pattern value="\d+(\.\d+){1,3}" />
        </xs:restriction>
    </xs:simpleType>

    <!-- Task -->
    <xs:complexType name="taskType">
        <xs:all>
            <xs:element name="RegistrationInfo" type="registrationInfoType" minOccurs="0" />
            <xs:element name="Triggers"         type="triggersType"         minOccurs="0" />
            <xs:element name="Settings"         type="settingsType"         minOccurs="0" />
            <xs:element name="Data"             type="dataType"             minOccurs="0" />
            <xs:element name="Principals"       type="principalsType"       minOccurs="0" />
            <xs:element name="Actions"          type="actionsType" />
        </xs:all>
        <xs:attribute name="version" use="optional" fixed="1.3" type="versionType" />
    </xs:complexType>

    <!-- RegistrationInfo -->
    <xs:complexType name="registrationInfoType">
        <xs:all>
            <xs:element name="URI"                type="xs:anyURI"                  minOccurs="0" />
            <xs:element name="SecurityDescriptor" type="xs:string"                  minOccurs="0" />
            <xs:element name="Source"             type="xs:string"                  minOccurs="0" />
            <xs:element name="Date"               type="xs:dateTime"                minOccurs="0" />
            <xs:element name="Author"             type="xs:string"                  minOccurs="0" />
            <xs:element name="Version"            type="xs:string"                  minOccurs="0" />
            <xs:element name="Description"        type="xs:string"                  minOccurs="0" />
            <xs:element name="Documentation"      type="xs:string"                  minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- Triggers -->
    <xs:complexType name="triggersType">
        <xs:group ref="triggerGroup" minOccurs="0" maxOccurs="48"/>
    </xs:complexType>
    <xs:group name="triggerGroup">
        <xs:choice>
            <xs:element name="BootTrigger"               type="bootTriggerType"               minOccurs="0" />
            <xs:element name="RegistrationTrigger"       type="registrationTriggerType"       minOccurs="0" />
            <xs:element name="IdleTrigger"               type="idleTriggerType"               minOccurs="0" />
            <xs:element name="TimeTrigger"               type="timeTriggerType"               minOccurs="0" />
            <xs:element name="EventTrigger"              type="eventTriggerType"              minOccurs="0" />
            <xs:element name="LogonTrigger"              type="logonTriggerType"              minOccurs="0" />
            <xs:element name="SessionStateChangeTrigger" type="sessionStateChangeTriggerType" minOccurs="0" />
            <xs:element name="CalendarTrigger"           type="calendarTriggerType"           minOccurs="0" />
        </xs:choice>
    </xs:group>

    <!-- Base type for all triggers -->
    <xs:complexType name="triggerBaseType" abstract="true">
        <xs:sequence>
            <xs:element name="Enabled"            type="xs:boolean"     default="true"  minOccurs="0" />
            <xs:element name="StartBoundary"      type="xs:dateTime"                    minOccurs="0" />
            <xs:element name="EndBoundary"        type="xs:dateTime"                    minOccurs="0" />
            <xs:element name="Repetition"         type="repetitionType"                 minOccurs="0" />
            <xs:element name="ExecutionTimeLimit" type="xs:duration"    default="PT72H" minOccurs="0" />
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="optional" />
    </xs:complexType>

    <!-- Repetition -->
    <xs:complexType name="repetitionType">
        <xs:all>
            <xs:element name="Interval">
                <xs:simpleType>
                    <xs:restriction base="xs:duration">
                        <xs:minInclusive value="PT1M"/>
                        <xs:maxInclusive value="P31D"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="Duration" minOccurs="0">
                <xs:simpleType>
                    <xs:restriction base="xs:duration">
                        <xs:minInclusive value="PT1M"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="StopAtDurationEnd"    type="xs:boolean" default="false" minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- BootTrigger -->
    <xs:complexType name="bootTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType">
                <xs:sequence>
                    <xs:element name="Delay"        type="xs:duration" default="PT0M" minOccurs="0" />
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
   
    <!-- RegistrationTrigger -->
    <xs:complexType name="registrationTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType">
                <xs:sequence>
                    <xs:element name="Delay" type="xs:duration" default="PT0M" minOccurs="0" />
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>

    <!-- IdleTrigger -->
    <xs:complexType name="idleTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType" />
        </xs:complexContent>
    </xs:complexType>

    <!-- TimeTrigger -->
    <xs:complexType name="timeTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType">
                <xs:sequence>
                    <xs:element name="RandomDelay"  type="xs:duration" default="PT0M" minOccurs="0" />
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>    
 
    <!--valueQueries-->   
    <xs:complexType name="namedValues">
         <xs:sequence>
             <xs:element name="Value" type="namedValue" minOccurs="1" maxOccurs="32"/>
         </xs:sequence>
    </xs:complexType>       
      
    <xs:complexType name="namedValue">
         <xs:simpleContent>
             <xs:extension base="nonEmptyString">
                 <xs:attribute name="name" type="nonEmptyString" use="required" />
             </xs:extension>
         </xs:simpleContent>
    </xs:complexType>

    <!-- EventTrigger -->
    <xs:complexType name="eventTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType">
                <xs:sequence>
                    <xs:element name="Subscription" type="nonEmptyString" />
                    <xs:element name="Delay"        type="xs:duration" default="PT0M" minOccurs="0" />
                    <xs:element name="PeriodOfOccurrence"  type="xs:duration" default="PT0M" minOccurs="0" />
                    <xs:element name="NumberOfOccurrences" default="1" minOccurs="0">
                        <xs:simpleType>
                            <xs:restriction base="xs:unsignedByte">
                                <xs:minInclusive value="1"/>
                                <xs:maxInclusive value="32"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:element>
                    <xs:element name="MatchingElement" type="nonEmptyString" minOccurs="0" />
                    <xs:element name="ValueQueries" type="namedValues" minOccurs="0" />              
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>    

    <!-- LogonTrigger -->
    <xs:complexType name="logonTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType">
                <xs:sequence>
                    <xs:element name="UserId"   type="nonEmptyString" minOccurs="0" maxOccurs="1" />
                    <xs:element name="Delay"    type="xs:duration" default="PT0M" minOccurs="0" />
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>

    <!-- SessionStateChangeTrigger -->
    <xs:simpleType name="sessionStateChangeType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="ConsoleConnect" />
            <xs:enumeration value="ConsoleDisconnect" />
            <xs:enumeration value="RemoteConnect" />
            <xs:enumeration value="RemoteDisconnect" />
            <xs:enumeration value="SessionLock"  />
            <xs:enumeration value="SessionUnlock" />
        </xs:restriction>
    </xs:simpleType>

    <xs:complexType name="sessionStateChangeTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType">
                <xs:sequence>
                    <xs:element name="UserId"      type="nonEmptyString"                        minOccurs="0" maxOccurs="1"/>
                    <xs:element name="Delay"       type="xs:duration"            default="PT0M" minOccurs="0" />
                    <xs:element name="StateChange" type="sessionStateChangeType"                minOccurs="1" maxOccurs="1"/>
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>


    <!-- CalendarTrigger -->
    <xs:complexType name="calendarTriggerType">
        <xs:complexContent>
            <xs:extension base="triggerBaseType">
                <xs:sequence>
                    <xs:element name="RandomDelay"  type="xs:duration" default="PT0M" minOccurs="0" />
                    <xs:choice>
                        <xs:element name="ScheduleByDay"            type="dailyScheduleType" />
                        <xs:element name="ScheduleByWeek"           type="weeklyScheduleType" />
                        <xs:element name="ScheduleByMonth"          type="monthlyScheduleType" />
                        <xs:element name="ScheduleByMonthDayOfWeek" type="monthlyDayOfWeekScheduleType" />
                    </xs:choice>
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>

    <!-- DailySchedule -->
    <xs:complexType name="dailyScheduleType">
        <xs:all>
            <xs:element name="DaysInterval" minOccurs="0">
                <xs:simpleType>
                    <xs:restriction base="xs:unsignedInt">
                        <xs:minInclusive value="1"/>
                        <xs:maxInclusive value="365"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
        </xs:all>
    </xs:complexType>

    <!-- WeeklySchedule -->
    <xs:complexType name="weeklyScheduleType">
        <xs:all>
            <xs:element name="WeeksInterval" minOccurs="0">
                <xs:simpleType>
                    <xs:restriction base="xs:unsignedByte">
                        <xs:minInclusive value="1"/>
                        <xs:maxInclusive value="52"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="DaysOfWeek" type="daysOfWeekType" minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- MonthlySchedule -->
    <xs:complexType name="monthlyScheduleType">
        <xs:all>
            <xs:element name="DaysOfMonth" type="daysOfMonthType" minOccurs="0" />
            <xs:element name="Months" type="monthsType" minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- MonthlyDayOfWeekSchedule -->
    <xs:complexType name="monthlyDayOfWeekScheduleType">
        <xs:all>
            <xs:element name="Weeks"        type="weeksType" minOccurs="0" />
            <xs:element name="DaysOfWeek"   type="daysOfWeekType" />
            <xs:element name="Months"       type="monthsType" minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- DaysOfWeek -->
    <xs:complexType name="daysOfWeekType">
        <xs:all>
            <xs:element name="Monday"       fixed="" minOccurs="0" />
            <xs:element name="Tuesday"      fixed="" minOccurs="0" />
            <xs:element name="Wednesday"    fixed="" minOccurs="0" />
            <xs:element name="Thursday"     fixed="" minOccurs="0" />
            <xs:element name="Friday"       fixed="" minOccurs="0" />
            <xs:element name="Saturday"     fixed="" minOccurs="0" />
            <xs:element name="Sunday"       fixed="" minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- Months -->
    <xs:complexType name="monthsType">
        <xs:all>
            <xs:element name="January"      fixed="" minOccurs="0" />
            <xs:element name="February"     fixed="" minOccurs="0" />
            <xs:element name="March"        fixed="" minOccurs="0" />
            <xs:element name="April"        fixed="" minOccurs="0" />
            <xs:element name="May"          fixed="" minOccurs="0" />
            <xs:element name="June"         fixed="" minOccurs="0" />
            <xs:element name="July"         fixed="" minOccurs="0" />
            <xs:element name="August"       fixed="" minOccurs="0" />
            <xs:element name="September"    fixed="" minOccurs="0" />
            <xs:element name="October"      fixed="" minOccurs="0" />
            <xs:element name="November"     fixed="" minOccurs="0" />
            <xs:element name="December"     fixed="" minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- DaysOfMonth -->
    <xs:complexType name="daysOfMonthType">
        <xs:sequence>
            <xs:element name="Day" type="dayOfMonthType" minOccurs="0" maxOccurs="32" />
        </xs:sequence>    
    </xs:complexType>
    <xs:simpleType name="dayOfMonthType">
        <xs:restriction base="xs:string">
            <xs:pattern value="[1-9]|[1-2][0-9]|3[0-1]|Last" />
        </xs:restriction>
    </xs:simpleType>

    <!-- Weeks -->
    <xs:complexType name="weeksType">
        <xs:sequence>
            <xs:element name="Week" type="weekType" minOccurs="0" maxOccurs="5" />
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="weekType">
        <xs:restriction base="xs:string">
            <xs:pattern value="[1-4]|Last" />
        </xs:restriction>
    </xs:simpleType>

    <!-- Settings -->
    <xs:complexType name="settingsType">
        <xs:all>
            <xs:element name="AllowStartOnDemand"               type="xs:boolean"                   default="true"      minOccurs="0" />
            <xs:element name="RestartOnFailure"                 type="restartType"                                      minOccurs="0" />
            <xs:element name="MultipleInstancesPolicy"          type="multipleInstancesPolicyType"  default="IgnoreNew" minOccurs="0" />
            <xs:element name="DisallowStartIfOnBatteries"       type="xs:boolean"                   default="true"      minOccurs="0" />
            <xs:element name="StopIfGoingOnBatteries"           type="xs:boolean"                   default="true"      minOccurs="0" />
            <xs:element name="AllowHardTerminate"               type="xs:boolean"                   default="true"      minOccurs="0" />
            <xs:element name="StartWhenAvailable"               type="xs:boolean"                   default="false"     minOccurs="0" />
            <xs:element name="NetworkProfileName"               type="xs:string"                                        minOccurs="0" />
            <xs:element name="RunOnlyIfNetworkAvailable"        type="xs:boolean"                   default="false"     minOccurs="0" />
            <xs:element name="WakeToRun"                        type="xs:boolean"                   default="false"     minOccurs="0" />
            <xs:element name="Enabled"                          type="xs:boolean"                   default="true"      minOccurs="0" />
            <xs:element name="Hidden"                           type="xs:boolean"                   default="false"     minOccurs="0" />
            <xs:element name="DeleteExpiredTaskAfter"           type="xs:duration"                  default="PT0S"      minOccurs="0" />
            <xs:element name="IdleSettings"                     type="idleSettingsType"                                 minOccurs="0" />
            <xs:element name="NetworkSettings"                  type="networkSettingsType"                              minOccurs="0" />
            <xs:element name="ExecutionTimeLimit"               type="xs:duration"                  default="PT72H"     minOccurs="0" />
            <xs:element name="Priority"                         type="priorityType"                 default="7"         minOccurs="0" />
            <xs:element name="RunOnlyIfIdle"                    type="xs:boolean"                   default="false"     minOccurs="0" />
            <xs:element name="UseUnifiedSchedulingEngine"       type="xs:boolean"                   default="false"     minOccurs="0" />
            <xs:element name="DisallowStartOnRemoteAppSession"  type="xs:boolean"                   default="false"     minOccurs="0" />
        </xs:all>
    </xs:complexType>
    
    <!-- MultipleInstancesPolicy -->
    <xs:simpleType name="multipleInstancesPolicyType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="Parallel" />
            <xs:enumeration value="Queue" />
            <xs:enumeration value="IgnoreNew" />
            <xs:enumeration value="StopExisting" />
        </xs:restriction>
    </xs:simpleType>

    <!-- Lower number means higher priority. -->
    <xs:simpleType name="priorityType">
        <xs:restriction base="xs:byte">
            <xs:minInclusive value="0" fixed="true" />
            <xs:maxInclusive value="10" fixed="true" />
        </xs:restriction>
    </xs:simpleType>

    <!-- IdleSettings -->
    <xs:complexType name="idleSettingsType">
        <xs:all>
            <xs:element name="Duration" default="PT10M" minOccurs="0">
                <xs:simpleType>
                    <xs:restriction base="xs:duration">
                        <xs:minInclusive value="PT1M"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="WaitTimeout" default="PT1H"  minOccurs="0">
                <xs:simpleType>
                    <xs:restriction base="xs:duration">
                        <xs:minInclusive value="PT1M"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="StopOnIdleEnd" type="xs:boolean"  default="true"  minOccurs="0" />
            <xs:element name="RestartOnIdle" type="xs:boolean"  default="false" minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- NetworkSettings -->
    <xs:complexType name="networkSettingsType">
        <xs:all>
            <xs:element name="Name" type="nonEmptyString" minOccurs="0" />
            <xs:element name="Id"   type="guidType"       minOccurs="0" />
        </xs:all>
    </xs:complexType>

    <!-- RestartOnFailure -->
    <xs:complexType name="restartType">
        <xs:all>
            <xs:element name="Interval">
                <xs:simpleType>
                    <xs:restriction base="xs:duration">
                        <xs:minInclusive value="PT1M"/>
                        <xs:maxInclusive value="P31D"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="Count">
                <xs:simpleType>
                    <xs:restriction base="xs:unsignedByte">
                        <xs:minInclusive value="1"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
        </xs:all>
    </xs:complexType>

    <!-- Data -->
    <xs:complexType name="dataType">
        <xs:sequence>
            <xs:any />
        </xs:sequence>
    </xs:complexType>

    <!-- Principals -->
    <xs:complexType name="principalsType">
        <xs:sequence>
            <xs:element name="Principal" type="principalType" maxOccurs="1" />
        </xs:sequence>
    </xs:complexType>

    <!-- Principal -->
    <xs:complexType name="principalType">
        <xs:all>
            <xs:element name="UserId" type="nonEmptyString" minOccurs="0" />
            <xs:element name="LogonType" type="logonType" minOccurs="0" maxOccurs="1"/>
            <xs:element name="GroupId" type="nonEmptyString" minOccurs="0" />
            <xs:element name="DisplayName" type="xs:string" minOccurs="0" />
            <xs:element name="RunLevel" type="runLevelType" minOccurs="0" maxOccurs="1"/>
            <xs:element name="ProcessTokenSidType" type="processTokenSidType" minOccurs="0" maxOccurs="1"/>
            <xs:element name="RequiredPrivileges" type="requiredPrivilegesType" minOccurs="0" />
        </xs:all>
        <xs:attribute name="id" type="xs:ID" use="optional" />
    </xs:complexType>
    <xs:simpleType name="logonType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="S4U" />
            <xs:enumeration value="Password" />
            <xs:enumeration value="InteractiveToken" />
            <!-- for backward compatibility -->
            <xs:enumeration value="InteractiveTokenOrPassword" />
        </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="runLevelType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="LeastPrivilege" />
            <xs:enumeration value="HighestAvailable" />
        </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="processTokenSidType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="None" />
            <xs:enumeration value="Unrestricted" />
        </xs:restriction>
    </xs:simpleType>
   
    <xs:complexType name="requiredPrivilegesType">
         <xs:sequence>
             <xs:element name="Privilege" type="privilegeType" minOccurs="1" maxOccurs="64"/>
         </xs:sequence>
    </xs:complexType>       

    <xs:simpleType name="privilegeType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="SeCreateTokenPrivilege" />
            <xs:enumeration value="SeAssignPrimaryTokenPrivilege" />
            <xs:enumeration value="SeLockMemoryPrivilege" />
            <xs:enumeration value="SeIncreaseQuotaPrivilege" />
            <xs:enumeration value="SeUnsolicitedInputPrivilege" />
            <xs:enumeration value="SeMachineAccountPrivilege" />
            <xs:enumeration value="SeTcbPrivilege" />
            <xs:enumeration value="SeSecurityPrivilege" />
            <xs:enumeration value="SeTakeOwnershipPrivilege" />
            <xs:enumeration value="SeLoadDriverPrivilege" />
            <xs:enumeration value="SeSystemProfilePrivilege" />
            <xs:enumeration value="SeSystemtimePrivilege" />
            <xs:enumeration value="SeProfileSingleProcessPrivilege" />
            <xs:enumeration value="SeIncreaseBasePriorityPrivilege" />
            <xs:enumeration value="SeCreatePagefilePrivilege" />
            <xs:enumeration value="SeCreatePermanentPrivilege" />
            <xs:enumeration value="SeBackupPrivilege" />
            <xs:enumeration value="SeRestorePrivilege" />
            <xs:enumeration value="SeShutdownPrivilege" />
            <xs:enumeration value="SeDebugPrivilege" />
            <xs:enumeration value="SeAuditPrivilege" />
            <xs:enumeration value="SeSystemEnvironmentPrivilege" />
            <xs:enumeration value="SeChangeNotifyPrivilege" />
            <xs:enumeration value="SeRemoteShutdownPrivilege" />
            <xs:enumeration value="SeUndockPrivilege" />
            <xs:enumeration value="SeSyncAgentPrivilege" />
            <xs:enumeration value="SeEnableDelegationPrivilege" />
            <xs:enumeration value="SeManageVolumePrivilege" />
            <xs:enumeration value="SeImpersonatePrivilege" />
            <xs:enumeration value="SeCreateGlobalPrivilege" />
            <xs:enumeration value="SeTrustedCredManAccessPrivilege" />
            <xs:enumeration value="SeRelabelPrivilege" />
            <xs:enumeration value="SeIncreaseWorkingSetPrivilege" />
            <xs:enumeration value="SeTimeZonePrivilege" />
            <xs:enumeration value="SeCreateSymbolicLinkPrivilege" />
        </xs:restriction>
    </xs:simpleType>

    <!-- Actions -->
    <xs:complexType name="actionsType">
        <xs:sequence>
            <xs:group ref="actionGroup" maxOccurs="32" />
        </xs:sequence>
        <xs:attribute name="Context" type="xs:IDREF" use="optional" />
    </xs:complexType>
    <xs:group name="actionGroup">
        <xs:choice>
            <xs:element name="Exec"          type="execType" />
            <xs:element name="ComHandler"    type="comHandlerType" />
            <xs:element name="SendEmail"     type="sendEmailType" />
            <xs:element name="ShowMessage"   type="showMessageType" />
        </xs:choice>
    </xs:group>

    <!-- Base type for actions. -->
    <xs:complexType name="actionBaseType" abstract="true">
        <xs:attribute name="id" type="xs:ID" use="optional" />
    </xs:complexType>

    <!-- Exec -->
    <xs:complexType name="execType">
        <xs:complexContent>
            <xs:extension base="actionBaseType">
                <xs:all>
                    <xs:element name="Command"          type="pathType"/>
                    <xs:element name="Arguments"        type="xs:string" minOccurs="0"/>
                    <xs:element name="WorkingDirectory" type="pathType" minOccurs="0"/>
                </xs:all>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>

    <!-- ComHandler -->
    <xs:complexType name="comHandlerType">
        <xs:complexContent>
            <xs:extension base="actionBaseType">
                <xs:all>
                    <xs:element name="ClassId"  type="guidType" />
                    <xs:element name="Data"     type="dataType" minOccurs="0" />
                </xs:all>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>

    <xs:simpleType name="guidType">
        <xs:restriction base="xs:string">
            <!-- GUID should be in a form:
                    {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
                 where x is a hexadecimal digit. -->
            <xs:pattern value="\{([0-9a-fA-F]){8}(\-[0-9a-fA-F]{4}){3}\-[0-9a-fA-F]{12}\}" />
        </xs:restriction>
    </xs:simpleType>

    <!-- SendEmail -->
    <xs:complexType name="sendEmailType">
        <xs:complexContent>
            <xs:extension base="actionBaseType">
                <xs:all>
                    <xs:element name="Server"       type="nonEmptyString" />
                    <xs:element name="Subject"      type="xs:string"        minOccurs="0" />
                    <xs:element name="To"           type="xs:string"        minOccurs="0" />
                    <xs:element name="Cc"           type="xs:string"        minOccurs="0" />
                    <xs:element name="Bcc"          type="xs:string"        minOccurs="0" />
                    <xs:element name="ReplyTo"      type="xs:string"        minOccurs="0" />
                    <xs:element name="From"         type="xs:string"        minOccurs="0" />
                    <xs:element name="HeaderFields" type="headerFieldsType" minOccurs="0" />
                    <xs:element name="Body"         type="xs:string"        minOccurs="0" />
                    <xs:element name="Attachments"  type="attachmentsType"  minOccurs="0" />
                </xs:all>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>

    <xs:complexType name="headerFieldsType">
        <xs:sequence>
            <xs:element name="HeaderField"  type="headerFieldType"  minOccurs="0"   maxOccurs="32"/>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="headerFieldType">
        <xs:all>
            <xs:element name="Name"         type="nonEmptyString" />
            <xs:element name="Value"        type="xs:string" />
        </xs:all>
    </xs:complexType>

    <xs:complexType name="attachmentsType">
        <xs:sequence>
            <xs:element name="File"  type="nonEmptyString"  minOccurs="0"   maxOccurs="8"/>
        </xs:sequence>
    </xs:complexType>

    <!-- ShowMessage -->
    <xs:complexType name="showMessageType">
        <xs:complexContent>
            <xs:extension base="actionBaseType">
                <xs:all>
                    <xs:element name="Title"  type="nonEmptyString" />
                    <xs:element name="Body"   type="nonEmptyString" />
                </xs:all>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>

</xs:schema>
```



 

 




