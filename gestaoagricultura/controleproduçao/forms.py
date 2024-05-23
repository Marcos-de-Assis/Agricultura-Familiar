from django import forms
from .models import Producao

class ProducaoForm(forms.ModelForm):
    class Meta:
        model = Producao
        fields = [
            'modelo_producao', 'categoria_producao', 'inicio_producao', 'tipo_cult_plantada',
            'area_cultivada', 'mudas_plantada', 'quant_sementes', 'valor_muda', 'fertilizante',
            'tipo_fertil', 'quant_fertilizante', 'valor_unid_fertil', 'defensivo', 'tipo_defensivo',
            'quant_defensivo', 'valor_defensivo', 'quant_agua', 'custo_irrigacao', 'preparo_solo',
            'custo_pre_solo', 'analise_solo', 'custo_anal_solo', 'conser_solo', 'dat_colheta',
            'quant_produzida', 'quant_vendida', 'val_unid_vendida', 'tipo_armazen', 'cust_armazen',
            'cust_mao_obra', 'manut_equipament', 'cust_energia', 'cust_transport', 'regist_certificado',
            'cust_certificado', 'tipo_animal', 'quant_animal', 'tipo_alimento', 'quant_aliment',
            'valor_aliment', 'saude_animal', 'cust_saude', 'tipo_prod_animal', 'dat_venda_animal',
            'quant_vend_animal', 'venda_unit_animal', 'certif_animal', 'cust_certif_animal', 'observacao'
        ]
        