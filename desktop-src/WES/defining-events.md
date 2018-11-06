---
title: Defining Events
description: Providers must define all the events that they write. To define an event, use the event element.
ms.assetid: f282612c-cfa5-42fe-af8a-5b35c033abe2
ms.topic: article
ms.date: 05/31/2018
---

# Defining Events

Providers must define all the events that they write. To define an event, use the **event** element.

The **value** attribute is the event identifier and it must be unique for the events that you define. Whether you set the other attributes depends on who will be consuming the events and from where. If administrators will be consuming your events using a tool like Windows Event Viewer, then you must set the **channel** attribute. If the channel type is Admin, then you must also specify the **level** attribute and set it to one of the levels defined in Winmeta.xml (win:Critical through win:Informational).

If the event contains event-specific data, you must set the **template** attribute to the identifier of the template that defines the event-specific data. The **level**, **keywords**, **task**, and **opcode** attributes are used to group or bucket events. Although these attributes are optional, you should consider specifying level, task, and opcode, so that consumers can easily access only those events of interest. The **level** and **keywords** attributes can also be used by an ETW tracing session to limit the events that are written to the event tracing log file. The **keywords** attribute contains a space-delimited list of keyword names defined in the manifest.

You should set the **symbol** attribute to specify the symbolic constant that the compiler generates to identify the event's event descriptor—you use the event descriptor when writing the event. If you do not specify the symbol, the compiler will generate a name for you.

The **message** attribute contains the localized message string that is displayed with the event. To include event-specific data in the string, add insertion strings to the message text. For example, to include the third data item in the template, include %3.

The following example shows how to define events.


```XML
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="http://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"    
    >

    <instrumentation>
        <events>
            <provider name="Microsoft-Windows-SampleProvider" 
                guid="{1db28f2e-8f80-4027-8c5a-a11f7f10f62d}" 
                symbol="PROVIDER_GUID" 
                resourceFileName="<path to the exe or dll that contains the metadata resources>" 
                messageFileName="<path to the exe or dll that contains the string resources>"
                message="$(string.Provider.Name)">

                <channels>
                    <channel chid="c1" 
                             name="Microsoft-Windows-SampleProvider/Admin"
                             type="Admin"
                             enabled="true">

                    <channel chid="c2" 
                             name="Microsoft-Windows-SampleProvider/Operational"
                             type="Operational"
                             enabled="true">
                </channels>

                <tasks>
                    <task />
 
                    <task name="Transfer" 
                          symbol="TASK_TRANSFER"
                          value="0" 
                          message="$(string.Task.Transfer)">

                        <opcodes>
                            <opcode name="Download" 
                                    symbol="OPCODE_DOWNLOAD_XFER" 
                                    value="11"
                                    message="$(string.Task.Transfer.Download)"/>
                            <opcode name="Upload" 
                                    symbol="OPCODE_UPLOAD_XFER" 
                                    value="12"
                                    message="$(string.Task.Transfer.Upload)"/>
                            <opcode name="UploadReply" 
                                    symbol="OPCODE_UPLOADREPLY_XFER" 
                                    value="13"
                                    message="$(string.Task.Transfer.UploadReply)"/>
                        </opcodes>
                    </task>

                    <task name="Validate" 
                          symbol="TASK_VALIDATE"
                          value="2" 
                          message="$(string.Validate)">

                        <opcodes>
                            <opcode name="GetRules" 
                                    symbol="OPCODE_GET_RULES" 
                                    value="11"
                                    message="$(string.Validate.GetRules)"/>
                        </opcodes>
                    </task>
                </tasks>

                <opcodes>
                    <opcode name="Initialize" 
                            symbol="OPCODE_INITIALIZE" 
                            value="12"
                            message="$(string.Initialize)"/>

                    <opcode name="Cleanup" 
                            symbol="OPCODE_CLEANUP" 
                            value="13"
                            message="$(string.Cleanup)"/>
                 </opcodes>

                <maps>
                    <valueMap name="TransferType">
                        <map value="1" message="$(string.TransferType.Download)"/>
                        <map value="2" message="$(string.TransferType.Upload)"/>
                        <map value="3" message="$(string.TransferType.UploadReply)"/>
                    </valueMap>
                    <bitMap name="DaysOfTheWeek">
                        <map value="0x1" message="$(string.DaysOfTheWeek.Sunday)"/>
                        <map value="0x2" message="$(string.DaysOfTheWeek.Monday)"/>
                        <map value="0x4" message="$(string.DaysOfTheWeek.Tuesday)"/>
                        <map value="0x8" message="$(string.DaysOfTheWeek.Wednesday)"/>
                        <map value="0x10" message="$(string.DaysOfTheWeek.Thursday)"/>
                        <map value="0x20" message="$(string.DaysOfTheWeek.Friday)"/>
                        <map value="0x40" message="$(string.DaysOfTheWeek.Saturday)"/>
                    </bitMap>
                </maps>

                <templates>
                    <template tid="t2">
                        <data name="TransferName" inType="win:UnicodeString"/>
                        <data name="TransferType" inType="win:UInt32" map="TransferType"/>
                        <data name="Day" inType="win:UInt32" map="DaysOfTheWeek"/>
                    </template>

                    <template tid="t3">
                        <data name="TransferName" inType="win:UnicodeString"/>
                        <data name="ErrorCode" inType="win:Int32" outType="win:HResult"/>
                        <data name="FilesCount" inType="win:UInt16" />
                        <data name="Files" inType="win:UnicodeString" count="FilesCount"/>
                   </template>

                    <template tid="t4">
                        <data name="FilesCount" inType="win:UInt16" />
                        <data name="Files" inType="win:UnicodeString" count="FilesCount"/>
                        <data name="Path" inType="win:UnicodeString" />
                    </template>
                </templates>

                <events>
                    <event value="1" 
                        level="win:Informational" 
                        task="Transfer"
                        template="t2" 
                        channel="c2" 
                        symbol="TRANSFER_SCHEDULE_EVENT"
                        message ="$(string.Event.XferSchedule)"/>

                    <event value="2" 
                        level="win:Error" 
                        task="Transfer"
                        opcode="Download"
                        template="t3" 
                        channel="c1" 
                        symbol="DOWNLOAD_XFER_FAILED_EVENT"
                        message ="$(string.Event.DownloadFailed)"/>

                    <event value="3" 
                        level="win:Warning" 
                        task="Transfer"
                        opcode="Cleanup"
                        template="t4" 
                        channel="c1" 
                        symbol="TEMPFILE_CLEANUP_EVENT"
                        message ="$(string.Event.TempFilesNotDeleted)"/>
                </events>

            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>
                <string id="Provider.Name" value="Sample Provider"/>

                <string id="Task.Transfer" value="Transfer"/>
                <string id="Task.Transfer.Download" value="Download transfer operation"/>
                <string id="Task.Transfer.Upload" value="Upload transfer operation"/>
                <string id="Task.Transfer.UploadReply" value="Upload-reply transfer operation"/>

                <string id="TransferType.Download" value="download"/>
                <string id="TransferType.Upload" value="upload"/>
                <string id="TransferType.UploadReply" value="upload-reply"/>

                <string id="DaysOfTheWeek.Sunday" value="Sunday"/>
                <string id="DaysOfTheWeek.Monday" value="Monday"/>
                <string id="DaysOfTheWeek.Tuesday" value="Tuesday"/>
                <string id="DaysOfTheWeek.Wednesday" value="Wednesday"/>
                <string id="DaysOfTheWeek.Thursday" value="Thursday"/>
                <string id="DaysOfTheWeek.Friday" value="Friday"/>
                <string id="DaysOfTheWeek.Saturday" value="Saturday"/>

                <string id="Event.XferSchedule" value="The %1 %2 transfer will occur on %3."/>
                <string id="Event.DownloadFailed" value="The %1 download job failed with %2. The job contains the following files:%n%n%4"/>
                <string id="Event.TempFilesNotDeleted" value="The following temp files were not removed from %3:%n%n%2"/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```



 

 




