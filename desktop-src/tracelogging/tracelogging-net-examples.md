---
title: .NET TraceLogging Examples
description:
  This topic contains a .NET TraceLogging example that illustrates how to log an
  event only when the session verbosity level is verbose, and how to log
  structured event data.
ms.assetid: 156016FE-FDC7-4361-BFD0-5F41254FE14D
ms.topic: article
ms.date: 06/06/2022
---

# .NET TraceLogging Examples

This topic contains a .NET TraceLogging example that illustrates how to log an
event only when the session verbosity level is verbose, and how to log
structured event data.

```CSharp
using System;
using System.Text;
using System.Diagnostics.Tracing;

namespace MoreSimpleTraceLoggingExamples
{
    class Program
    {
        private static EventSource log = new EventSource(
            "SimpleTraceLoggingProvider",
            EventSourceSettings.EtwSelfDescribingEventFormat);

        static void Main(string[] args)
        {
            StringBuilder cmdLine = new StringBuilder();
            foreach (string arg in args)
            {
                cmdLine.AppendFormat("{0} ", arg);
            }

            // Log event verbosity level and opcode
            // This event is only logged when the session verbosity level is verbose.
            log.Write("CmdLine", new EventSourceOptions {Level=EventLevel.Verbose, Opcode=EventOpcode.Info },
                                 new { Args = cmdLine.ToString().TrimEnd() });

            try
            {
                int j = 0;
                int i = 1 / j;
            }
            catch (Exception e)
            {
                var error = new Error { ErrorTitle = e.Message, CallStack = e.StackTrace, ErrType = ErrorType.Exception };
                log.Write("Error", new { Error = error, ErrorType = e.ToString() });
            }
        }
    }

    [EventData] // [EventData] makes it possible to pass an instance of the class as an argument to EventSource.Write()
    public class Error
    {
        public string ErrorTitle { get; set; }
        public string CallStack { get; set; }
        public ErrorType ErrType { get; set; }
    }

    public enum ErrorType
    {
        Exception,
        UserError,
        ProgramError
    }
}
```
