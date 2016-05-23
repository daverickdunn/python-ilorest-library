 # Copyright 2016 Hewlett Packard Enterprise Development LP
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.

import sys
from redfishobject import RedfishObject
from ilorest.rest.v1_helper import ServerDownOrUnreachableError

def ex23_dump_ilo_event_log(redfishobj):
    sys.stdout.write("\nEXAMPLE 23: Dump iLO Event Log\n")
    instances = redfishobj.search_for_type("LogService.")

    for instance in instances:
        if instance["@odata.id"].endswith("IEL/"):
            tmp = redfishobj.redfish_get(instance["@odata.id"])
            rsp = redfishobj.redfish_get(tmp.dict["Entries"]["@odata.id"])

            for entry in rsp.dict["Members"]:
                response = redfishobj.redfish_get(entry["@odata.id"])
                sys.stdout.write(response.dict["Message"] + "\n")

if __name__ == "__main__":
    # When running on the server locally use the following commented values
    # iLO_host = "blobstore://."
    # iLO_account = "None"
    # iLO_password = "None"

    # When running remotely connect using the iLO address, iLO account name, 
    # and password to send https requests
    iLO_host = "https://16.83.63.43"
    iLO_account = "admin"
    iLO_password = "password"

    # Create a REDFISH object
    try:
        REDFISH_OBJ = RedfishObject(iLO_host, iLO_account, iLO_password)
    except ServerDownOrUnreachableError, excp:
        sys.stderr.write("ERROR: server not reachable or doesn't support " \
                                                                "RedFish.\n")
        sys.exit()
    except Exception, excp:
        raise excp

    ex23_dump_ilo_event_log(REDFISH_OBJ)
  