#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import sys
import os

class ZombieCloud:
    def __init__(self):
        self.day = 1
        self.survival_score = 75  # 初期生存率スコア
        self.max_days = 7
        self.preparations = {
            "auto_healing": False,
            "monitoring": False,
            "backup": False,
            "security": False
        }
        self.events_history = []
        self.database_corrupted = False  # 3日目のイベント用フラグ
        self.network_isolated = False    # 4日目のイベント用フラグ
        self.ddos_mitigated = False      # 5日目のイベント用フラグ
        self.credentials_leaked = False  # 6日目のイベント用フラグ
        self.amazon_q_dependency = 0     # Amazon Qへの依存度カウンター
        
    def clear_screen(self):
        """画面をクリアする"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def slow_print(self, text, delay=0.03):
        """テキストをタイプライター風に表示"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def display_header(self):
        """ゲームのヘッダーを表示"""
        self.clear_screen()
        print("\n" + "=" * 80)
        print(f"{'ゾンビクラウド 〜停止するサービス、迫る障害〜':^80}")
        print(f"{'DAY ' + str(self.day) + ' / ' + str(self.max_days):^80}")
        print("=" * 80 + "\n")
        
    def display_status(self):
        """現在のステータスを表示"""
        print("\n" + "-" * 80)
        print(f"クラウド生存率: {self.survival_score}%")
        
        # 生存率に応じたステータスメッセージ
        if self.survival_score >= 80:
            status = "【安定】サービス正常稼働中"
        elif self.survival_score >= 50:
            status = "【警告】一部サービスに遅延あり"
        elif self.survival_score >= 30:
            status = "【危険】複数のサービスがダウン中"
        else:
            status = "【緊急】大規模障害発生中！"
            
        print(f"ステータス: {status}")
        print("-" * 80 + "\n")
        
    def get_player_choice(self, options):
        """プレイヤーの選択を取得"""
        valid_choices = list(options.keys())
        
        while True:
            choice = input("\n選択してください (A/B/C/D): ").strip().upper()
            if choice in valid_choices:
                return choice
            else:
                print("無効な選択です。A, B, C, D のいずれかを入力してください。")
                
    def update_score(self, points):
        """スコアを更新し、結果を表示"""
        old_score = self.survival_score
        self.survival_score = max(0, min(100, self.survival_score + points))
        
        if points > 0:
            print(f"\n🔼 クラウド生存率が {abs(points)}% 上昇しました！ ({old_score}% → {self.survival_score}%)")
        elif points < 0:
            print(f"\n🔽 クラウド生存率が {abs(points)}% 低下しました... ({old_score}% → {self.survival_score}%)")
        else:
            print(f"\nクラウド生存率に変化はありません。 ({self.survival_score}%)")
    def day_one(self):
        """1日目: 準備日"""
        self.display_header()
        
        self.slow_print("あなたは大手企業のクラウドインフラ担当者。")
        time.sleep(0.5)
        self.slow_print("最近、他社のクラウドサービスで「ゾンビプロセス」と呼ばれる謎の障害が発生し、")
        self.slow_print("次々とシステムを侵食しているという噂が広まっています。")
        time.sleep(0.5)
        self.slow_print("\n上司: 「念のため、うちのシステムも対策しておいてくれ。何が起きるかわからないからな。」")
        self.slow_print("\nあなたは明日から始まるかもしれない障害に備えて、今日は準備を行うことにしました。")
        
        self.display_status()
        
        options = {
            "A": "Auto Healing機能を有効化する（障害発生時に自動復旧）",
            "B": "詳細なモニタリングとアラート設定を強化する",
            "C": "重要データのバックアップを取っておく",
            "D": "Amazon Qに相談: 「クラウドシステムの障害対策で最も効果的なのは？」"
        }
        
        print("どのような準備を行いますか？")
        for key, value in options.items():
            print(f"{key}: {value}")
            
        choice = self.get_player_choice(options)
        
        if choice == "A":
            self.slow_print("\nあなたはEC2、RDS、Lambda関数などにAuto Healing機能を設定しました。")
            self.slow_print("障害が発生した際に自動的に復旧するよう設定が完了しました。")
            self.preparations["auto_healing"] = True
            self.update_score(5)
            
        elif choice == "B":
            self.slow_print("\nCloudWatchダッシュボードを作成し、重要メトリクスのアラートを設定しました。")
            self.slow_print("異常な動作を素早く検知できるようになりました。")
            self.preparations["monitoring"] = True
            self.update_score(5)
            
        elif choice == "C":
            self.slow_print("\n重要なデータベースとファイルのバックアップを作成し、別リージョンにレプリケーションしました。")
            self.slow_print("最悪の事態でもデータは守られるでしょう。")
            self.preparations["backup"] = True
            self.update_score(5)
            
        elif choice == "D":
            self.slow_print("\nAmazon Qからの回答:")
            self.slow_print("「効果的なクラウド障害対策には多層防御が重要です。具体的には:")
            self.slow_print("1. 複数のアベイラビリティゾーンにわたるデプロイ")
            self.slow_print("2. 自動スケーリングとヘルスチェックの実装")
            self.slow_print("3. 定期的なバックアップと災害復旧計画")
            self.slow_print("4. 包括的なモニタリングとアラート設定")
            self.slow_print("これらを組み合わせることで、障害への耐性が大幅に向上します。」")
            
            self.slow_print("\nあなたはアドバイスに従い、セキュリティ設定を強化しました。")
            self.preparations["security"] = True
            self.update_score(5)
            self.amazon_q_dependency += 1
            
        self.slow_print("\n準備を終えたあなたは、明日に備えて一旦休憩することにしました。")
        self.slow_print("しかし、不安な予感は拭えません...")
        
        input("\n[Enterキーを押して次の日へ進む]")
        
    def day_two(self):
        """2日目: 最初の障害日"""
        self.display_header()
        
        self.slow_print("朝、あなたのスマートフォンが鳴り響きます。")
        time.sleep(0.5)
        self.slow_print("\n上司: 「大変だ！EC2インスタンスの一部が応答しなくなっている！")
        self.slow_print("      ログを見ると、謎のプロセスがCPUを100%食い尽くしているぞ！」")
        time.sleep(0.5)
        self.slow_print("\nモニターを確認すると、確かに複数のインスタンスが赤く点滅しています。")
        self.slow_print("ログには「ZOMBIE_PROCESS_DETECTED」という不気味なメッセージが...")
        
        self.display_status()
        
        options = {
            "A": "影響を受けているインスタンスを強制再起動する",
            "B": "セキュリティグループを厳格化し、不要な通信を遮断する",
            "C": "様子を見る（自然に回復するかもしれない）",
            "D": "Amazon Qに相談: 「EC2インスタンスが謎のプロセスでCPU100%になっています。対処法は？」"
        }
        
        print("どのように対応しますか？")
        for key, value in options.items():
            print(f"{key}: {value}")
            
        choice = self.get_player_choice(options)
        
        # 1日目の準備状況に基づいて結果を変える
        if choice == "A":
            self.slow_print("\nあなたは影響を受けているインスタンスを強制再起動しました。")
            
            if self.preparations["auto_healing"]:
                self.slow_print("初日に設定したAuto Healing機能のおかげで、インスタンスは正常な状態で起動しました！")
                self.slow_print("ゾンビプロセスは消滅し、システムは正常に戻りました。")
                self.update_score(10)
            else:
                self.slow_print("インスタンスは再起動しましたが、数分後に再び同じ症状が現れました。")
                self.slow_print("ゾンビプロセスは消えず、むしろ他のインスタンスにも広がり始めています...")
                self.update_score(-15)
                
        elif choice == "B":
            self.slow_print("\nあなたはセキュリティグループのルールを厳格化し、不要な通信を遮断しました。")
            
            if self.preparations["security"]:
                self.slow_print("初日に強化したセキュリティ設定と組み合わさり、効果的な防御壁ができました！")
                self.slow_print("ゾンビプロセスの通信が遮断され、新たな感染は止まりました。")
                self.update_score(15)
            else:
                self.slow_print("通信は制限されましたが、すでに感染したインスタンスは影響を受けていません。")
                self.slow_print("問題は部分的に緩和されましたが、完全には解決していません。")
                self.update_score(-5)
                
        elif choice == "C":
            self.slow_print("\nあなたは様子を見ることにしました。")
            self.slow_print("しかし、時間の経過とともに状況は悪化していきます...")
            self.slow_print("ゾンビプロセスは次々と他のインスタンスに広がり、システムリソースを食い尽くしています！")
            self.update_score(-25)
            
        elif choice == "D":
            self.slow_print("\nAmazon Qからの回答:")
            self.slow_print("「EC2インスタンスのCPU使用率が100%になる問題には、以下の対処法があります:")
            self.slow_print("1. 問題のプロセスを特定し、強制終了（kill -9 PID）")
            self.slow_print("2. インスタンスの再起動")
            self.slow_print("3. セキュリティグループの見直しと不審な通信の遮断")
            self.slow_print("4. CloudWatchログで原因となるイベントを特定」")
            
            self.amazon_q_dependency += 1
            
            if self.preparations["monitoring"]:
                self.slow_print("\nあなたは初日に設定した詳細なモニタリングデータを確認し、")
                self.slow_print("Amazon Qのアドバイスに従って問題のプロセスを特定・駆除しました。")
                self.slow_print("迅速な対応により、被害を最小限に抑えることができました！")
                self.update_score(20)
            else:
                self.slow_print("\nアドバイスは理解できましたが、詳細なモニタリングがないため")
                self.slow_print("問題の根本原因を特定するのに時間がかかってしまいました。")
                self.slow_print("その間にも感染は広がり、一部のサービスがダウンしてしまいました。")
                self.update_score(-10)
                
        self.slow_print("\n2日目が終わりました。明日はどんな障害が待ち受けているでしょうか...")
        
        input("\n[Enterキーを押して次の日へ進む]")
    def day_three(self):
        """3日目: データベース障害"""
        self.display_header()
        
        self.slow_print("朝のコーヒーを飲んでいると、緊急アラートが鳴り響きます。")
        time.sleep(0.5)
        self.slow_print("\n「警告: RDSインスタンスで異常なI/O活動を検出」")
        self.slow_print("\nデータベースコンソールを確認すると、主要なRDSインスタンスが赤く点滅しています。")
        self.slow_print("ログを見ると、データが徐々に破損していくような不可解な現象が...")
        self.slow_print("\n同僚: 「何かがデータベースを食べている...まるでゾンビのように...」")
        
        self.display_status()
        
        options = {
            "A": "データベースを最新のスナップショットから復元する",
            "B": "読み取り専用レプリカに切り替え、メインDBを隔離する",
            "C": "データベースエンジンのバージョンアップを試みる",
            "D": "Amazon Qに相談: 「RDSインスタンスでデータが破損しています。どうすれば？」"
        }
        
        print("どのように対応しますか？")
        for key, value in options.items():
            print(f"{key}: {value}")
            
        choice = self.get_player_choice(options)
        
        if choice == "A":
            self.slow_print("\nあなたは最新のスナップショットからデータベースの復元を開始しました。")
            
            if self.preparations["backup"]:
                self.slow_print("初日に作成した詳細なバックアップ計画のおかげで、最新の状態に復元できました！")
                self.slow_print("データの損失はほとんどなく、システムは正常に戻りました。")
                self.update_score(15)
                self.database_corrupted = False
            else:
                self.slow_print("スナップショットは3日前のもので、多くのデータが失われてしまいました。")
                self.slow_print("システムは動作していますが、重要なデータの一部が失われています...")
                self.update_score(-10)
                self.database_corrupted = True
                
        elif choice == "B":
            self.slow_print("\nあなたはトラフィックを読み取り専用レプリカに切り替え、メインDBを隔離しました。")
            
            if self.preparations["monitoring"]:
                self.slow_print("初日に設定した詳細なモニタリングのおかげで、問題の発生源を特定できました。")
                self.slow_print("レプリカへの切り替えはスムーズに行われ、サービスの中断を最小限に抑えられました。")
                self.update_score(10)
                self.database_corrupted = False
            else:
                self.slow_print("レプリカへの切り替えは成功しましたが、レプリカ自体も一部データが破損しています。")
                self.slow_print("読み取り専用モードで何とか動作していますが、完全な解決には至っていません。")
                self.update_score(-5)
                self.database_corrupted = True
                
        elif choice == "C":
            self.slow_print("\nあなたはデータベースエンジンのバージョンアップを試みました。")
            self.slow_print("しかし、バージョンアップ中にさらに多くのデータが破損してしまいました。")
            self.slow_print("システムは不安定な状態で、ユーザーからの苦情が殺到しています...")
            self.update_score(-20)
            self.database_corrupted = True
            
        elif choice == "D":
            self.slow_print("\nAmazon Qからの回答:")
            self.slow_print("「RDSデータ破損の問題には、以下の対処法があります:")
            self.slow_print("1. Point-in-Time Recoveryを使用して、問題発生前の状態に復元")
            self.slow_print("2. 読み取り専用レプリカがある場合は、それをプライマリに昇格")
            self.slow_print("3. バックアップから新しいインスタンスを作成し、データを検証")
            self.slow_print("4. AWS Database Migration Service (DMS)を使用してデータを救出」")
            
            self.amazon_q_dependency += 1
            
            # Amazon Qへの依存度が高まると、回答の質が低下する
            if self.amazon_q_dependency >= 3:
                self.slow_print("\nしかし、Amazon Qの回答を待っている間にも、データの破損は進行しています...")
                self.slow_print("回答を得た時には、すでに多くのデータが失われていました。")
                self.slow_print("対応が遅れたため、復旧は部分的にしか成功しませんでした。")
                self.update_score(-15)
                self.database_corrupted = True
            elif random.random() < 0.6:  # 60%の確率で成功
                self.slow_print("\nあなたはAmazon Qのアドバイスに従い、Point-in-Time Recoveryを実行しました。")
                self.slow_print("破損直前の状態にデータベースを復元することに成功！")
                self.slow_print("システムは正常に戻り、データの損失も最小限に抑えられました。")
                self.update_score(15)
                self.database_corrupted = False
            else:
                self.slow_print("\nAmazon Qのアドバイスに従おうとしましたが、")
                self.slow_print("Point-in-Time Recoveryの実行中にさらなるエラーが発生しました。")
                self.slow_print("復元は部分的にしか成功せず、一部のデータは失われてしまいました...")
                self.update_score(-10)
                self.database_corrupted = True
                
        self.slow_print("\n3日目が終わりました。データベースの危機は乗り越えましたが、")
        self.slow_print("ゾンビプロセスの脅威はまだ続いています...")
        
        input("\n[Enterキーを押して次の日へ進む]")
    def day_four(self):
        """4日目: ネットワーク障害"""
        self.display_header()
        
        self.slow_print("オフィスに着くと、すでに緊急事態が発生していました。")
        time.sleep(0.5)
        self.slow_print("\n上司: 「VPCが完全に分断されている！サブネット間の通信が全て遮断されているぞ！」")
        self.slow_print("\nネットワークダッシュボードを確認すると、通常は青く表示されるはずの接続線が")
        self.slow_print("全て赤く点滅しています。まるで血管が切断されたかのようです。")
        self.slow_print("\nログには「ZOMBIE_NETWORK_ISOLATION」という不気味なメッセージが...")
        
        self.display_status()
        
        options = {
            "A": "ルートテーブルとNACLを全て初期状態にリセットする",
            "B": "バックアップVPCを立ち上げ、トラフィックを切り替える",
            "C": "AWSサポートに緊急チケットを発行する",
            "D": "Amazon Qに相談: 「VPCが分断され、サブネット間通信ができません。対処法は？」"
        }
        
        print("どのように対応しますか？")
        for key, value in options.items():
            print(f"{key}: {value}")
            
        choice = self.get_player_choice(options)
        
        # 前日までの状況が影響する
        network_penalty = 0
        if self.database_corrupted:
            network_penalty -= 10
            self.slow_print("\n(昨日のデータベース問題が解決していないため、状況はより複雑になっています...)")
        
        if choice == "A":
            self.slow_print("\nあなたはルートテーブルとNACLを全て初期状態にリセットしました。")
            
            if self.preparations["security"]:
                self.slow_print("初日に強化したセキュリティ設定のバックアップがあったため、")
                self.slow_print("安全な初期状態に戻すことができました！")
                self.slow_print("ネットワーク接続が徐々に回復しています。")
                self.update_score(15 + network_penalty)
                self.network_isolated = False
            else:
                self.slow_print("リセットは部分的に成功しましたが、いくつかのルールが競合しています。")
                self.slow_print("一部のサブネットは依然として孤立したままです...")
                self.update_score(-5 + network_penalty)
                self.network_isolated = True
                
        elif choice == "B":
            self.slow_print("\nあなたはバックアップVPCを立ち上げ、トラフィックの切り替えを開始しました。")
            
            if self.preparations["auto_healing"]:
                self.slow_print("初日に設定したAuto Healing機能のおかげで、")
                self.slow_print("新しいVPCへの移行がスムーズに行われました！")
                self.slow_print("サービスの中断は最小限で済みました。")
                self.update_score(10 + network_penalty)
                self.network_isolated = False
            else:
                self.slow_print("バックアップVPCは立ち上がりましたが、設定が不完全です。")
                self.slow_print("移行中に多くのサービスが断続的にダウンしています...")
                self.update_score(-10 + network_penalty)
                self.network_isolated = True
                
        elif choice == "C":
            self.slow_print("\nあなたはAWSサポートに緊急チケットを発行しました。")
            
            # AWSサポートの対応は、Amazon Qへの依存度が高いほど遅くなる
            if self.amazon_q_dependency >= 3:
                self.slow_print("しかし、これまでAmazon Qに頼りすぎていたため、")
                self.slow_print("自分でのトラブルシューティングスキルが不足していることに気づきます。")
                self.slow_print("チケットの説明が不十分で、サポートからの返答に時間がかかっています...")
                self.update_score(-20 + network_penalty)
                self.network_isolated = True
            else:
                self.slow_print("チケットには詳細な状況と試した対策を記載しました。")
                self.slow_print("AWSサポートからの返答は数時間後に届き、適切な対応方法が示されました。")
                self.slow_print("指示に従って設定を修正し、ネットワークは徐々に回復しています。")
                self.update_score(-5 + network_penalty)
                self.network_isolated = False
            
        elif choice == "D":
            self.slow_print("\nAmazon Qからの回答:")
            self.slow_print("「VPC分断の問題には、以下の対処法があります:")
            self.slow_print("1. セキュリティグループとNACLの設定を確認し、不正なルールを特定")
            self.slow_print("2. VPCフローログを分析して異常なトラフィックパターンを特定")
            self.slow_print("3. Transit Gatewayの設定を確認し、ルーティングテーブルを修正")
            self.slow_print("4. 最後の手段として、新しいVPCを作成し移行を検討」")
            
            self.amazon_q_dependency += 1
            
            # Amazon Qへの依存度が高まると、回答の質が低下する
            if self.amazon_q_dependency >= 4:
                self.slow_print("\nしかし、Amazon Qの回答は一般的すぎて、あなたの特殊な状況には適用できません。")
                self.slow_print("回答を理解して実装している間にも、ネットワークの分断は広がっています...")
                self.slow_print("対応が遅れ、多くのサービスがダウンしてしまいました。")
                self.update_score(-20 + network_penalty)
                self.network_isolated = True
            elif self.preparations["monitoring"]:
                self.slow_print("\nあなたは初日に設定した詳細なモニタリングデータを確認し、")
                self.slow_print("Amazon Qのアドバイスに従って問題のルールを特定・修正しました。")
                self.slow_print("VPCフローログの分析により、ゾンビプロセスの通信パターンを遮断することに成功！")
                self.update_score(20 + network_penalty)
                self.network_isolated = False
            else:
                self.slow_print("\nアドバイスは理解できましたが、詳細なモニタリングがないため")
                self.slow_print("問題の根本原因を特定するのに時間がかかってしまいました。")
                self.slow_print("一部のネットワーク接続は回復しましたが、完全な解決には至っていません...")
                self.update_score(-5 + network_penalty)
                self.network_isolated = True
                
        self.slow_print("\n4日目が終わりました。ネットワークの危機との戦いは続きます...")
        
        input("\n[Enterキーを押して次の日へ進む]")
    def day_five(self):
        """5日目: DDoS攻撃"""
        self.display_header()
        
        self.slow_print("深夜、あなたの電話が鳴り響きます。")
        time.sleep(0.5)
        self.slow_print("\n上司: 「大変だ！何者かが私たちのロードバランサーに大規模なDDoS攻撃を仕掛けている！」")
        self.slow_print("\nダッシュボードを確認すると、トラフィックが通常の100倍以上に急増しています。")
        self.slow_print("CloudWatchグラフは天井知らずに上昇し、アラームが次々と鳴り響いています。")
        self.slow_print("\nログには「ZOMBIE_BOTNET_ATTACK」という不気味なメッセージが...")
        
        self.display_status()
        
        options = {
            "A": "AWS Shield Advancedを緊急で有効化する",
            "B": "WAFでレート制限とIPブロックを設定する",
            "C": "CloudFrontディストリビューションを前面に配置する",
            "D": "Amazon Qに相談: 「大規模なDDoS攻撃を受けています。緊急対策は？」"
        }
        
        print("どのように対応しますか？")
        for key, value in options.items():
            print(f"{key}: {value}")
            
        choice = self.get_player_choice(options)
        
        # 前日までの状況が影響する
        ddos_penalty = 0
        if self.network_isolated:
            ddos_penalty -= 15
            self.slow_print("\n(昨日のネットワーク問題が解決していないため、対応が困難になっています...)")
        
        if choice == "A":
            self.slow_print("\nあなたはAWS Shield Advancedを緊急で有効化しました。")
            self.slow_print("高額な費用がかかりますが、今は生き残ることが最優先です。")
            
            if random.random() < 0.8:  # 80%の確率で成功
                self.slow_print("Shield Advancedの保護が有効になり、DDoS攻撃は徐々に緩和されています！") self.slow_print("トラフィックが正常値に戻りつつあります。") self.update_score(15 + ddos_penalty)
                self.ddos_mitigated = True
            else:
                self.slow_print("Shield Advancedの設定に時間がかかり、その間にもサービスはダウンし続けています...")
                self.slow_print("攻撃は部分的に緩和されましたが、まだ完全には収まっていません。")
                self.update_score(-5 + ddos_penalty)
                self.ddos_mitigated = False
                
        elif choice == "B":
            self.slow_print("\nあなたはWAFでレート制限とIPブロックの設定を急いで行いました。")
            
            if self.preparations["security"]:
                self.slow_print("初日に強化したセキュリティ設定のおかげで、")
                self.slow_print("効果的なWAFルールをすぐに適用することができました！")
                self.slow_print("不正なトラフィックがブロックされ、サービスは回復しつつあります。")
                self.update_score(20 + ddos_penalty)
                self.ddos_mitigated = True
            else:
                self.slow_print("WAFルールの設定は部分的に成功しましたが、攻撃の一部は依然として通過しています。")
                self.slow_print("サービスは不安定な状態が続いています...")
                self.update_score(-10 + ddos_penalty)
                self.ddos_mitigated = False
                
        elif choice == "C":
            self.slow_print("\nあなたはCloudFrontディストリビューションを急いで設定し、前面に配置しました。")
            
            if self.preparations["auto_healing"]:
                self.slow_print("初日に設定したAuto Healing機能と組み合わせることで、")
                self.slow_print("CloudFrontの設定がスムーズに行われました！")
                self.slow_print("エッジロケーションでトラフィックが分散され、攻撃の影響が軽減されています。")
                self.update_score(10 + ddos_penalty)
                self.ddos_mitigated = True
            else:
                self.slow_print("CloudFrontの設定中にエラーが発生し、完全に機能していません。")
                self.slow_print("攻撃は続いており、サービスの大部分がダウンしています...")
                self.update_score(-15 + ddos_penalty)
                self.ddos_mitigated = False
                
        elif choice == "D":
            self.slow_print("\nAmazon Qからの回答:")
            self.slow_print("「DDoS攻撃への緊急対策としては:")
            self.slow_print("1. AWS Shield Advancedを有効化して専門家の支援を受ける")
            self.slow_print("2. WAFでレート制限とIPレピュテーションベースのルールを適用")
            self.slow_print("3. CloudFrontとRoute 53を使用してトラフィックを分散")
            self.slow_print("4. Auto Scalingを設定して容量を一時的に増やす」")
            
            self.amazon_q_dependency += 1
            
            # DDoS攻撃は即時対応が必要なため、Amazon Qに相談している時間的猶予がない
            self.slow_print("\nしかし、Amazon Qの回答を待っている間にも、攻撃は激しさを増しています...")
            self.slow_print("対応が遅れたため、多くのサービスがすでにダウンしてしまいました。")
            self.slow_print("回答を得た時には、すでに大きな被害が出ていました。")
            self.update_score(-25 + ddos_penalty)
            self.ddos_mitigated = False
                
        self.slow_print("\n5日目が終わりました。DDoS攻撃との戦いは続きますが、")
        self.slow_print("ゾンビクラウドの正体が少しずつ見えてきました...")
        
        input("\n[Enterキーを押して次の日へ進む]")
    def day_six(self):
        """6日目: 認証情報漏洩"""
        self.display_header()
        
        self.slow_print("朝、緊急セキュリティアラートが鳴り響きます。")
        time.sleep(0.5)
        self.slow_print("\n「警告: 複数のIAMユーザーで不審なアクティビティを検出」")
        self.slow_print("\nCloudTrailログを確認すると、複数のIAMユーザーが同時に")
        self.slow_print("通常とは異なるリージョンからAPIコールを行っています。")
        self.slow_print("\nさらに恐ろしいことに、S3バケットの設定が次々と変更され、")
        self.slow_print("データが外部に流出している形跡があります。")
        self.slow_print("\nログには「ZOMBIE_CREDENTIAL_BREACH」という不気味なメッセージが...")
        
        self.display_status()
        
        options = {
            "A": "全てのIAMアクセスキーを無効化し、新しいキーを発行する",
            "B": "CloudTrailログを分析し、不正アクセスの範囲を特定する",
            "C": "S3バケットを一時的に非公開設定に変更する",
            "D": "Amazon Qに相談: 「IAM認証情報が漏洩した可能性があります。対処法は？」"
        }
        
        print("どのように対応しますか？")
        for key, value in options.items():
            print(f"{key}: {value}")
            
        choice = self.get_player_choice(options)
        
        # 前日までの状況が影響する
        security_penalty = 0
        if not self.ddos_mitigated:
            security_penalty -= 15
            self.slow_print("\n(昨日のDDoS攻撃が続いているため、セキュリティ対応が困難になっています...)")
        
        if choice == "A":
            self.slow_print("\nあなたは全てのIAMアクセスキーを無効化し、新しいキーの発行を開始しました。")
            
            if self.preparations["security"]:
                self.slow_print("初日に強化したセキュリティ設定のおかげで、")
                self.slow_print("キーローテーションがスムーズに行われました！")
                self.slow_print("不正アクセスは遮断され、システムは安全な状態に戻りつつあります。")
                self.update_score(20 + security_penalty)
                self.credentials_leaked = False
            else:
                self.slow_print("キーの無効化は成功しましたが、新しいキーの配布に混乱が生じています。")
                self.slow_print("一部のサービスが認証エラーで停止しています...")
                self.update_score(-10 + security_penalty)
                self.credentials_leaked = True
                
        elif choice == "B":
            self.slow_print("\nあなたはCloudTrailログの詳細な分析を開始しました。")
            
            if self.preparations["monitoring"]:
                self.slow_print("初日に設定した詳細なモニタリングのおかげで、")
                self.slow_print("不正アクセスの正確な範囲と影響を特定することができました！")
                self.slow_print("影響を受けたリソースのみを対象に、効率的な対策を実施しています。")
                self.update_score(15 + security_penalty)
                self.credentials_leaked = False
            else:
                self.slow_print("ログの分析には時間がかかり、その間にも不正アクセスは続いています。")
                self.slow_print("影響の全容を把握しきれず、対応が後手に回っています...")
                self.update_score(-15 + security_penalty)
                self.credentials_leaked = True
                
        elif choice == "C":
            self.slow_print("\nあなたはS3バケットを一時的に全て非公開設定に変更しました。")
            self.slow_print("これにより、データの流出は止まりましたが、")
            self.slow_print("多くのサービスが正常に機能しなくなりました。")
            self.slow_print("ユーザーからの苦情が殺到しています...")
            self.update_score(-20 + security_penalty)
            self.credentials_leaked = True
            
        elif choice == "D":
            self.slow_print("\nAmazon Qからの回答:")
            self.slow_print("「IAM認証情報漏洩への対処法としては:")
            self.slow_print("1. 影響を受けた可能性のあるすべてのアクセスキーを無効化")
            self.slow_print("2. CloudTrailで不正なアクティビティを特定し、影響範囲を評価")
            self.slow_print("3. 多要素認証(MFA)を全ユーザーに強制適用")
            self.slow_print("4. AWS Organizationsのサービスコントロールポリシー(SCP)で制限を適用」")
            
            self.amazon_q_dependency += 1
            
            # セキュリティインシデントでは迅速な対応が必要
            if self.amazon_q_dependency >= 3:
                self.slow_print("\nAmazon Qの回答を待っている間にも、攻撃者は権限を拡大しています...")
                self.slow_print("回答を得た時には、すでに多くのリソースにアクセスされていました。")
                self.slow_print("対応が遅れたため、重要なデータが流出してしまいました。")
                self.update_score(-30 + security_penalty)
                self.credentials_leaked = True
            else:
                self.slow_print("\nあなたはAmazon Qのアドバイスを参考にしつつ、")
                self.slow_print("まず全てのIAMアクセスキーを無効化し、不正アクセスを遮断しました。")
                self.slow_print("その後、CloudTrailログを分析して影響範囲を特定しています。")
                self.update_score(-5 + security_penalty)
                self.credentials_leaked = False
                
        self.slow_print("\n6日目が終わりました。セキュリティ侵害との戦いは続きますが、")
        self.slow_print("明日が最後の戦いになるでしょう...")
        
        input("\n[Enterキーを押して次の日へ進む]")
    def day_seven(self):
        """7日目: 最終決戦"""
        self.display_header()
        
        self.slow_print("最終日、あなたのオフィスに緊張が漂っています。")
        time.sleep(0.5)
        self.slow_print("\n上司: 「ついに分かったぞ。このゾンビプロセスの正体は、")
        self.slow_print("      古いAIモデルが暴走して生まれた自己複製型のマルウェアだ！」")
        time.sleep(0.5)
        self.slow_print("\nモニターには全てのAWSサービスが赤く点滅し、")
        self.slow_print("「ZOMBIE_CLOUD_FINAL_FORM」というメッセージが表示されています。")
        self.slow_print("\n上司: 「これが最後の戦いだ。全てを賭けて対抗しよう！」")
        
        self.display_status()
        
        options = {
            "A": "全システムを一旦シャットダウンし、クリーンな状態から再起動する",
            "B": "災害復旧計画を発動し、バックアップサイトに切り替える",
            "C": "祈る（もはや人知を超えた存在に対抗するには神頼みしかない）",
            "D": "Amazon Qに相談: 「自己複製型マルウェアがAWS環境全体に広がっています。最終対策は？」"
        }
        
        print("最後の決断、どうしますか？")
        for key, value in options.items():
            print(f"{key}: {value}")
            
        choice = self.get_player_choice(options)
        
        # これまでの全ての準備と対応が影響する
        final_bonus = 0
        preparation_count = sum(1 for prep in self.preparations.values() if prep)
        final_bonus += preparation_count * 5
        
        if not self.database_corrupted:
            final_bonus += 10
        if not self.network_isolated:
            final_bonus += 10
        if self.ddos_mitigated:
            final_bonus += 10
        if not self.credentials_leaked:
            final_bonus += 10
            
        if choice == "A":
            self.slow_print("\nあなたは大胆な決断を下し、全システムの一時シャットダウンを開始しました。")
            self.slow_print("「全てを止めて、クリーンな状態から再構築する」")
            
            if final_bonus >= 30:  # 十分な準備と対応ができていた場合
                self.slow_print("\nこれまでの適切な準備と対応のおかげで、シャットダウンと再起動は整然と進みました。")
                self.slow_print("ゾンビプロセスが活動できない環境を作り出すことに成功！")
                self.slow_print("システムが一つずつ正常に戻っていきます。")
                self.update_score(25)
            else:
                self.slow_print("\nシャットダウンは成功しましたが、再起動に問題が発生しています。")
                self.slow_print("一部のシステムでデータの整合性が失われ、復旧が困難になっています...")
                self.update_score(-15)
                
        elif choice == "B":
            self.slow_print("\nあなたは災害復旧計画を発動し、バックアップサイトへの切り替えを開始しました。")
            
            if self.preparations["backup"]:
                self.slow_print("初日に作成した詳細なバックアップ計画のおかげで、")
                self.slow_print("別リージョンの環境にスムーズに切り替えることができました！")
                self.slow_print("クリーンな環境でサービスが再開され、ユーザーへの影響は最小限に抑えられています。")
                self.update_score(30)
            else:
                self.slow_print("バックアップサイトへの切り替えを試みましたが、準備が不十分でした。")
                self.slow_print("多くのデータが失われ、サービスの復旧には長い時間がかかりそうです...")
                self.update_score(-20)
                
        elif choice == "C":
            self.slow_print("\nあなたは椅子に深く腰掛け、目を閉じて祈り始めました。")
            self.slow_print("「どうか、この危機を乗り越えられますように...」")
            time.sleep(1)
            
            self.slow_print("\n...しかし、コンピュータの神様は忙しかったようです。")
            self.slow_print("モニターには次々とエラーメッセージが表示され、")
            self.slow_print("システムは完全に制御不能な状態になっていきます...")
            self.update_score(-40)
            
        elif choice == "D":
            self.slow_print("\nAmazon Qからの回答:")
            self.slow_print("「自己複製型マルウェアへの最終対策としては:")
            self.slow_print("1. 感染したリソースを特定し、完全に隔離")
            self.slow_print("2. クリーンなバックアップから新環境を構築")
            self.slow_print("3. WAF、Shield、GuardDutyなどの複数のセキュリティサービスを組み合わせて防御")
            self.slow_print("4. インフラをコードとして管理し、宣言的な状態を強制適用」")
            
            self.amazon_q_dependency += 1
            
            # Amazon Qへの依存度が高すぎると、自分で考える力が低下している
            if self.amazon_q_dependency >= 5:
                self.slow_print("\nこれまでAmazon Qに頼りすぎたため、あなた自身の判断力が鈍っています。")
                self.slow_print("回答を得ても、具体的にどう実装すればよいのか分からず、混乱しています。")
                self.slow_print("対応が遅れ、システムは次々とダウンしていきました...")
                self.update_score(-35)
            elif final_bonus >= 25:  # これまでの対応が十分だった場合
                self.slow_print("\nあなたはAmazon Qのアドバイスと、これまでの経験を組み合わせました。")
                self.slow_print("感染したリソースを特定・隔離し、クリーンな環境を迅速に構築！")
                self.slow_print("さらに、複数のセキュリティレイヤーを適用して防御を固めました。")
                self.slow_print("\nゾンビプロセスは徐々に弱まり、ついに消滅しました！")
                self.update_score(35)
            else:
                self.slow_print("\nAmazon Qのアドバイスは理解できましたが、")
                self.slow_print("これまでの対応の遅れにより、実行するのが困難になっています。")
                self.slow_print("一部のシステムは救出できましたが、多くは失われてしまいました...")
                self.update_score(-10)
                
        self.slow_print("\n7日間の戦いが終わりました。")
        self.slow_print("あなたのクラウドの運命は、これまでの選択によって決まりました...")
        
        input("\n[Enterキーを押してエンディングへ]")
    def run_game(self):
        """ゲームのメインループ"""
        self.display_welcome()
        
        while self.day <= self.max_days:
            if self.day == 1:
                self.day_one()
            elif self.day == 2:
                self.day_two()
            elif self.day == 3:
                self.day_three()
            elif self.day == 4:
                self.day_four()
            elif self.day == 5:
                self.day_five()
            elif self.day == 6:
                self.day_six()
            elif self.day == 7:
                self.day_seven()
            
            self.day += 1
                
        self.display_ending()
        
    def display_welcome(self):
        """ゲーム開始時のウェルカムメッセージ"""
        self.clear_screen()
        print("\n" + "=" * 80)
        print(f"{'ゾンビクラウド 〜停止するサービス、迫る障害〜':^80}")
        print("=" * 80)
        
        self.slow_print("\nようこそ、クラウドエンジニア。")
        self.slow_print("あなたは今から7日間、謎の「ゾンビプロセス」と戦うことになります。")
        self.slow_print("日々発生する障害に対処し、クラウドシステムを守り抜きましょう。")
        self.slow_print("\n選択次第で、あなたの運命は大きく変わります...")
        
        input("\n[Enterキーを押してゲームを開始]")
        
    def display_ending(self):
        """エンディングの表示"""
        self.display_header()
        
        print("\n7日間の戦いが終わりました。")
        
        # Amazon Qへの依存度が高すぎる場合の特殊エンディング
        if self.amazon_q_dependency >= 5:
            print("\n=== Amazon Q依存症エンディング ===")
            print("あなたはAmazon Qに頼りすぎるあまり、自分自身の技術力が低下してしまいました。")
            print("緊急時に自分で判断できず、常にAIの回答を待つようになってしまいました。")
            print("上司はあなたを見て嘆きます。「AIに頼るのは良いが、自分の頭で考えることも大切だ...」")
            print("\n最終スコア: " + str(self.survival_score) + "%")
            input("\n[Enterキーを押して終了]")
            return
        
        if self.survival_score >= 80:
            print("\n=== 完全復旧＆クラウド王 ===")
            print("あなたは見事にゾンビクラウドの危機を乗り越え、")
            print("システムを完全に復旧させました！")
            print("その卓越した技術と判断力は社内で称賛され、")
            print("「クラウド王」の異名を得ることになりました。")
            
        elif self.survival_score >= 40:
            print("\n=== 中途半端に生き延びる孤立クラウド ===")
            print("あなたは何とか主要システムを守り抜きましたが、")
            print("一部のサービスは失われてしまいました。")
            print("孤立したシステムで最低限の機能を維持しながら、")
            print("完全復旧への長い道のりが始まります...")
            
        else:
            print("\n=== 全滅 ===")
            print("ゾンビプロセスはシステム全体に広がり、")
            print("あなたの管理するクラウドは完全に機能を停止しました。")
            print("暗い画面を見つめるあなたの背後で、")
            print("サーバールームのドアがゆっくりと開く音が...")
            
        print("\nゲームオーバー")
        print(f"最終スコア: {self.survival_score}%")
        
        input("\n[Enterキーを押して終了]")

if __name__ == "__main__":
    game = ZombieCloud()
    game.run_game()

