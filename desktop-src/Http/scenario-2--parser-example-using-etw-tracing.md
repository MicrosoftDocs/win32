---
title: Scenario 2 Parser Example Using ETW Tracing
description: To generate an ETW trace report for the HTTP Server API component, run the steps as shown in the \ 0034;Generating an ETW Trace Report \ 0034; section of Scenario 1 HTTP Timeout Example Using ETW Tracing and Netsh Commands, but reproduce the error specific to this scenario.
ms.assetid: 2ccd2927-8a64-40a8-a29b-4b680a942f7f
ms.topic: article
ms.date: 05/31/2018
---

# Scenario 2: Parser Example Using ETW Tracing

To generate an ETW trace report for the HTTP Server API component, run the steps as shown in the "Generating an ETW Trace Report" section of [Scenario 1: HTTP Timeout Example Using ETW Tracing and Netsh Commands](scenario-1--http-timeout-example-using-etw-tracing-and-netsh-commands.md), but reproduce the error specific to this scenario. In this example, access the web application from a client machine, resulting in the "400 bad request" message being shown on the client. These steps are run on the server since it is hosting the web application.

## Viewing the Trace and Diagnosing

The resulting CSV file for traces can be viewed in Excel or any tool that supports the CSV format. Table 2 below shows excerpts from a sample trace file (httptrace.csv). In the trace report, the "Level" column shows an entry with a value of "2", which represents an error. As noted above, the HTTP Server API component follows the ETW Levels defined in the article [LevelType Complex Type Complex Type](../wes/eventmanifestschema-leveltype-complextype.md).

The ETW levels include: 1 Critical; 2 Error; 3 Warning; 4 Informational; 5 Verbose.

With this error, the event type (Type column) reports "ParseRequestFailed". In the subsequent columns for the ParseRequestFailed event, we see an "InvalidHost" entry. This entry means that the identified host in the HTTP Request is incorrect, according the HTTP protocol. Note the column with the "InvalidHost" entry is not included in the table for the sake of brevity and to avoid excerpting noncontiguous columns.

To fix this parsing issue, the web client should be corrected to be compliant with the HTTP RFC. 

| Event name                    | Type               | Event ID | Version | Channel | Level |
|-------------------------------|--------------------|----------|---------|---------|-------|
| EventTrace                    | Header             | 0        | 2       | 0       | 0     |
| Microsoft-Windows-HttpService | AddUrl             | 31       | 0       | 16      | 4     |
| Microsoft-Windows-HttpService | ConnConnect        | 21       | 0       | 16      | 4     |
| Microsoft-Windows-HttpService | ConnIdAssgn        | 22       | 0       | 16      | 4     |
| Microsoft-Windows-HttpService | RecvReq            | 1        | 0       | 16      | 4     |
| Microsoft-Windows-HttpService | ParseRequestFailed | 52       | 0       | 16      | 2     |
| Microsoft-Windows-HttpService | LogFileWrite       | 51       | 0       | 16      | 4     |



 

Table 2: Excerpts from a Sample Trace Report for a Parsing Issue

 

 