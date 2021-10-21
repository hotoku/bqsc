#!/bin/sh


curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"\`$GITHUB_BRANCH_NAME_SLUG\` failed PR auto-check! ($1)\"}" $SLACK_WEBHOOK_JDSC_ME
