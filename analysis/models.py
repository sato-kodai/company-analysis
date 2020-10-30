from django.db import models

class Company(models.Model):
    industry = models.CharField("業種", max_length=30, blank=False, null=True)
    code = models.CharField("証券コード", max_length=30, blank=False,null=True)
    name = models.CharField("会社名", max_length=30, blank=False)

    def __str__(self):
        return str(self.name)


class Statement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fiscal_year = models.CharField("決算年度", max_length=30)
    bs_current_assets = models.IntegerField("流動資産（百万円）", default=0)
    bs_fixed_assets = models.IntegerField("固定資産（百万円）", default=0)
    bs_current_liabilities = models.IntegerField("流動負債（百万円）", default=0)
    bs_fixed_liabilities = models.IntegerField("固定負債（百万円）", default=0)
    bs_net_assets = models.IntegerField("純資産（百万円）", default=0)
    pl_gross_sales = models.IntegerField("総売上（百万円）", default=0)
    pl_gross_profit = models.IntegerField("売上総利益（百万円）", default=0)
    pl_operating_profit = models.IntegerField("営業利益（百万円）", default=0)
    pl_ordinary_income = models.IntegerField("経常利益（百万円）", default=0)
    pl_income_before_tax = models.IntegerField("税引前当期純利益（百万円）", default=0)
    pl_net_income = models.IntegerField("当期純利益（百万円）", default=0)
    cf_operating = models.IntegerField("営業ＣＦ（百万円）", default=0)
    cf_investment = models.IntegerField("投資ＣＦ（百万円）", default=0)
    cf_finance = models.IntegerField("財務ＣＦ（百万円）", default=0)

    def __str__(self):
        return str(self.company) + '決算年度：【 ' + str(self.fiscal_year) + '】'

    # 総資産
    def bs_total_assets(self):
        f = self.bs_current_assets + self.bs_fixed_assets
        return f

    # 流動資産比率（流動資産／総資産）
    def current_assets_rate(self):
        try:
            f = self.bs_current_assets / self.bs_total_assets() * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 固定資産比率（固定資産／総資産）
    def fixed_assets_rate(self):
        try:
            f = self.bs_fixed_assets / self.bs_total_assets() * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 流動負債比率（流動負債／総資産）
    def current_liabilities_rate(self):
        try:
            f = self.bs_current_liabilities / self.bs_total_assets() * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 固定負債比率（固定負債／総資産）
    def fixed_liabilities_rate(self):
        try:
            f = self.bs_fixed_liabilities / self.bs_total_assets() * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 純資産比率（純資産／総資産）
    def net_assets_rate(self):
        try:
            f = self.bs_net_assets / self.bs_total_assets() * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 売上総利益率（売上総利益／総売上）
    def gross_profit_rate(self):
        try:
            f = self.pl_gross_profit / self.pl_gross_sales * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 営業利益率（営業利益／総売上）
    def operating_profit_rate(self):
        try:
            f = self.pl_operating_profit / self.pl_gross_sales * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 経常利益率（経常利益／総売上）
    def ordinary_income_rate(self):
        try:
            f = self.pl_ordinary_income / self.pl_gross_sales * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 税引前当期純利益率（税引前当期純利益／総売上）
    def income_before_tax_rate(self):
        try:
            f = self.pl_income_before_tax / self.pl_gross_sales * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # 当期純利益率（当期純利益／総売上）
    def net_income_rate(self):
        try:
            f = self.pl_net_income / self.pl_gross_sales * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # キャッシュフロー合計
    def cf_total_amount(self):
        f = self.cf_operating + self.cf_investment + self.cf_finance
        return f

    # 流動比率(流動資／流動負債)
    def current_rate(self):
        try:
            f = self.bs_current_assets / self.bs_current_liabilities * 100
        except ZeroDivisionError:
            f = '-'
        return f

    # ROE(営業利益／純資産)
    def roe(self):
        try:
            f = self.pl_operating_profit / self.bs_net_assets * 100
        except ZeroDivisionError:
            f = '-'
        return f

    #ROA(営業利益／純資産)
    def roa(self):
        try:
            f = self.pl_operating_profit / self.bs_total_assets() * 100
        except ZeroDivisionError:
            f = '-'
        return f