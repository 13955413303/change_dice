#!/d/project/env/python
# **********************************************
#
# v 1.0
#
# **********************************************
import sys
dicejson_path = r'change_dice.json'
stg_changelist = {
    'agent":':                                      ' 		"agent": "wss://agent.stg.lain.leyanbot.com/ws",\n',
    'authority":':                                  '		"authority": "https://stg-api.leyanbot.com/dice/v1",\n',
    'flashcard":':                                  '		"flashcard": "https://stg-api.leyanbot.com/flashcard/v1",\n',
    '"wingman":':                                   '		"wingman": "http://stg-pip-boy.infra.leyantech.com",\n',
    'endpoint": "https://api':                      '				"endpoint": "https://stg-api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote':                           '			"endpoint": "https://stg-bipolar-prokaryote.infra.leyantech.com/",\n'
}
prd_changelist = {
    'agent":':                                      ' 		"agent": "wss://agentproxy.leyanbot.com/ws",\n',
    'authority":':                                  '		"authority": "https://api.leyanbot.com/dice/v1",\n',
    'flashcard":':                                  '		"flashcard": "https://api.leyanbot.com/flashcard/v1",\n',
    '"wingman":':                                   '		"wingman": "https://wingman.leyantech.com",\n',
    'endpoint": "https://stg-api':                  '				"endpoint": "https://api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote':                           '			"endpoint": "https://bipolar-prokaryote.leyantech.com/",\n'
}

preview_changelist = {
    'agent":':                                      ' 		"agent": "wss://agentproxy.leyanbot.com/ws",\n',
    'authority":':                                  '		"authority": "https://api.leyanbot.com/dice/v1",\n',
    'flashcard":':                                  '		"flashcard": "https://api.leyanbot.com/flashcard/v1",\n',
    '"wingman":':                                   '		"wingman": "https://wingman.leyantech.com",\n',
    'endpoint": "https://stg-api':                  '				"endpoint": "https://api.leyanbot.com/dice/v1"\n',
    'bipolar-prokaryote':                           '			"endpoint": "https://preview-bipolar-prokaryote.infra.leyantech.com/",\n'
}


def change_json(env):
    content = open(dicejson_path, 'r',encoding='gbk').readlines()
    if env in ['stg', 'prd', 'preview']:
        changelist_name = env+'_changelist'
        env_list = globals()[changelist_name]
        for change in env_list:
            for line_con in content:
                if change in line_con:
                    line_num = content.index(line_con)
                    content[line_num] = env_list[change]
    else:
        print('input env error')

    open(dicejson_path, 'w').writelines(content)


try:
    change_json(sys.argv[1])
except BaseException:
    print('please input right info')
