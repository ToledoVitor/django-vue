#!/bin/bash
export COMPOSE_PROJECT_NAME=aplicativo_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run aplicativo unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
